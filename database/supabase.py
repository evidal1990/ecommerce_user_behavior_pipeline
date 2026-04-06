"""
Supabase PostgreSQL Connection Manager using psycopg2-binary

Prerequisites:
    pip install psycopg2-binary

Environment variables (recommended):
    SUPABASE_DB_HOST
    SUPABASE_DB_NAME
    SUPABASE_DB_USER
    SUPABASE_DB_PASSWORD
    SUPABASE_DB_PORT
"""

import os
import psycopg2
from psycopg2 import pool
from contextlib import contextmanager


class SupabaseConnectionManager:
    """
    Manages a connection pool to Supabase PostgreSQL.
    """

    def __init__(self):
        self._pool = None
        self._init_pool()

    def _init_pool(self):
        try:
            self._pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                host=os.getenv("SUPABASE_DB_HOST"),
                database=os.getenv("SUPABASE_DB_NAME"),
                user=os.getenv("SUPABASE_DB_USER"),
                password=os.getenv("SUPABASE_DB_PASSWORD"),
                port=os.getenv("SUPABASE_DB_PORT", 5432),
                sslmode="require",
            )
            if self._pool:
                print("Connection pool created successfully")
        except Exception as e:
            raise RuntimeError(f"Error creating connection pool: {e}")

    def get_connection(self):
        try:
            return self._pool.getconn()
        except Exception as e:
            raise RuntimeError(f"Error getting connection: {e}")

    def release_connection(self, conn) -> None:
        try:
            self._pool.putconn(conn)
        except Exception as e:
            raise RuntimeError(f"Error releasing connection: {e}")

    def close_all(self) -> None:
        try:
            self._pool.closeall()
        except Exception as e:
            raise RuntimeError(f"Error closing connections: {e}")

    @contextmanager
    def get_cursor(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise RuntimeError(f"Transaction error: {e}")
        finally:
            cursor.close()
            self.release_connection(conn)


# Example usage
if __name__ == "__main__":
    db = SupabaseConnectionManager()

    try:
        with db.get_cursor() as cur:
            cur.execute("SELECT NOW();")
            result = cur.fetchone()
            print("Current time from DB:", result)

    finally:
        db.close_all()
