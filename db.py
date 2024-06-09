import sqlite3
from utils.hashing import hash_password, check_password

def register_user(username, email, password):
    hashed_password = hash_password(password)
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

def login_user(email, password):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password(user[1], password):
        return user[0]
    return None
