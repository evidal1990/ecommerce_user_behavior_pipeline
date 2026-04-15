"""
Supabase PostgreSQL Connection Manager using psycopg2-binary (Session pooler).

Prerequisites:
    pip install psycopg2-binary

Environment variables:
    SUPABASE_POOLER_HOST — hostname do Session pooler (ex.: aws-0-...pooler.supabase.com)
    SUPABASE_DB_NAME, SUPABASE_DB_USER, SUPABASE_DB_PASSWORD
    SUPABASE_DB_PORT — opcional (por defeito 5432, típico do Session pooler)
    SUPABASE_DB_SSLMODE — opcional (por defeito require)
    SUPABASE_DB_GSSENCMODE — opcional (ex.: disable); se vazio, não é enviado ao cliente

Compatibilidade: se SUPABASE_POOLER_HOST estiver vazio, usa-se SUPABASE_DB_HOST
(útil durante migração de conexão directa para pooler).
"""

from __future__ import annotations

import logging
import os
import socket
from contextlib import contextmanager
from pathlib import Path

from dotenv import load_dotenv
from psycopg2 import pool

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_repo_env() -> None:
    """
    Carrega ``.env`` e ``.env.production`` na raiz do repositório.

    Usa ``override=True`` para que valores do projeto substituam variáveis já
    herdadas do processo (shell/IDE) — incluindo host vazio ou ``localhost``,
    que fazem o psycopg2 cair no socket local ``/tmp/.s.PGSQL.*``.
    Ordem: primeiro ``.env``, depois ``.env.production`` (este ganha em chaves repetidas).
    """
    for name in (".env", ".env.production"):
        path = _REPO_ROOT / name
        if path.is_file():
            load_dotenv(path, override=True)


def _ipv4_for_host(hostname: str) -> str | None:
    try:
        infos = socket.getaddrinfo(hostname, None, socket.AF_INET, socket.SOCK_STREAM)
    except OSError as exc:
        logger.warning("IPv4 lookup failed for %s: %s", hostname, exc)
        return None
    if not infos:
        return None
    sockaddr = infos[0][4]
    host_part = sockaddr[0]
    return str(host_part) if host_part is not None else None


def _db_connect_kwargs() -> dict:
    _load_repo_env()
    host = (
        os.getenv("SUPABASE_POOLER_HOST") or os.getenv("SUPABASE_DB_HOST") or ""
    ).strip()
    name = (os.getenv("SUPABASE_DB_NAME") or "").strip()
    user = (os.getenv("SUPABASE_DB_USER") or "").strip()
    password = os.getenv("SUPABASE_DB_PASSWORD")
    port_raw = (os.getenv("SUPABASE_DB_PORT") or "5432").strip()
    sslmode = (os.getenv("SUPABASE_DB_SSLMODE") or "require").strip()
    gssenc = (os.getenv("SUPABASE_DB_GSSENCMODE") or "").strip()

    if not host:
        env_files = [
            p.name
            for p in (_REPO_ROOT / ".env", _REPO_ROOT / ".env.production")
            if p.is_file()
        ]
        raise RuntimeError(
            "SUPABASE_POOLER_HOST (ou SUPABASE_DB_HOST) não está definido após carregar o .env. "
            f"Raiz esperada do repo: {_REPO_ROOT}. "
            f"Ficheiros encontrados: {env_files or 'nenhum'}. "
            "Sem host TCP explícito, o psycopg2 usa o socket local (/tmp/.s.PGSQL.*) e falha."
        )
    if not name or not user or password is None or password == "":
        raise RuntimeError(
            "Configuração incompleta: SUPABASE_DB_NAME, SUPABASE_DB_USER e "
            "SUPABASE_DB_PASSWORD têm de estar definidos.",
        )

    kwargs: dict = {
        "host": host,
        "database": name,
        "user": user,
        "password": password,
        "sslmode": sslmode,
        "connect_timeout": 15,
    }
    if port_raw:
        kwargs["port"] = int(port_raw)
    if gssenc:
        kwargs["gssencmode"] = gssenc

    ipv4 = _ipv4_for_host(host)
    if ipv4:
        kwargs["hostaddr"] = ipv4

    return kwargs


class SupabaseConnectionManager:
    """
    Gere um pool de ligações ao Postgres do Supabase via Session pooler.
    """

    def __init__(self) -> None:
        self._pool: pool.SimpleConnectionPool | None = None
        self._init_pool()

    def _init_pool(self) -> None:
        cfg: dict | None = None
        try:
            cfg = _db_connect_kwargs()
            self._pool = pool.SimpleConnectionPool(
                1,
                10,
                **cfg,
            )
            if self._pool:
                logger.info("Connection pool created successfully")
        except Exception as e:
            msg = str(e)
            if cfg is not None and (".s.PGSQL" in msg or "socket" in msg.lower()):
                msg = (
                    f"{msg} — Isto costuma indicar host vazio ou Postgres local. "
                    f"Host passado ao pool: {cfg.get('host')!r}. "
                    "Confirma SUPABASE_POOLER_HOST (Session pooler) no .env na raiz do repo."
                )
            raise RuntimeError(f"Error creating connection pool: {msg}") from e

    def get_connection(self):
        try:
            if self._pool is None:
                raise RuntimeError("Connection pool is not initialized")
            return self._pool.getconn()
        except Exception as e:
            raise RuntimeError(f"Error getting connection: {e}")

    def release_connection(self, conn) -> None:
        try:
            if self._pool is None:
                raise RuntimeError("Connection pool is not initialized")
            self._pool.putconn(conn)
        except Exception as e:
            raise RuntimeError(f"Error releasing connection: {e}")

    def close_all(self) -> None:
        try:
            if self._pool is None:
                return
            self._pool.closeall()
        except Exception as e:
            raise RuntimeError(f"Error closing connections: {e}")

    @contextmanager
    def get_cursor(self):
        conn = self.get_connection()
        cursor = None
        try:
            cursor = conn.cursor()
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise RuntimeError(f"Transaction error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            self.release_connection(conn)


if __name__ == "__main__":
    db = SupabaseConnectionManager()

    try:
        with db.get_cursor() as cur:
            cur.execute("SELECT NOW();")
            result = cur.fetchone()
            print("Current time from DB:", result)

    finally:
        db.close_all()
