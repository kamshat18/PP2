import psycopg2
from psycopg2 import sql

# Connect to your PostgreSQL database
def connect_db():
    return psycopg2.connect(
        dbname="postgres", 
        user="", 
        password="your_password", 
        host="localhost", 
        port="5432"
    )

# Create a new user if not exists
def get_or_create_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Check if user exists
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    if user:
        return user[0]  # Return user_id if exists
    else:
        cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
        return user_id
    
    cursor.close()
    conn.close()

# Get user's score and level
def get_user_score(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT level, score FROM user_scores WHERE user_id = %s ORDER BY date DESC LIMIT 1
    """, (user_id,))
    
    user_score = cursor.fetchone()
    conn.close()
    
    return user_score

# Save user progress (score and level)
def save_user_progress(user_id, level, score):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO user_scores (user_id, level, score) 
        VALUES (%s, %s, %s)
    """, (user_id, level, score))
    conn.commit()
    
    cursor.close()
    conn.close()
