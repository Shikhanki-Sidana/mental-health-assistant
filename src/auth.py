import hashlib
from db import get_connection

def register(username, password):
    conn = get_connection()
    cur = conn.cursor()
    h = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO users (username,password_hash) VALUES (%s,%s)", (username,h))
    conn.commit()
    conn.close()

def login(username, password):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    h = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("SELECT * FROM users WHERE username=%s AND password_hash=%s", (username,h))
    user = cur.fetchone()
    conn.close()
    return user
