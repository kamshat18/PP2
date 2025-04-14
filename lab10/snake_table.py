# db.py
import psycopg2
from psycopg2 import sql

def connect():
    return psycopg2.connect(
        database="postgres",
        user="postgres",
        password="12345678",
        host="localhost",
        port=5432
    )

def get_or_create_user(username):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            if result:
                user_id = result[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                user_id = cur.fetchone()[0]
                conn.commit()
    return user_id

def get_user_score(user_id):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT level, score FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
            result = cur.fetchone()
            if result:
                return result
    return (1, 0)  # уровень 1 и 0 очков по умолчанию

def save_user_progress(user_id, level, score):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_scores (user_id, level, score) VALUES (%s, %s, %s)
            """, (user_id, level, score))
            conn.commit()
