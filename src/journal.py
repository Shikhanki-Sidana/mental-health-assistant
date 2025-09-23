from db import get_connection

def add_entry(user_id, title, body, mood):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO journal_entries (user_id,title,body,mood_rating) VALUES (%s,%s,%s,%s)",
                (user_id,title,body,mood))
    conn.commit()
    conn.close()

def view_entries(user_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM journal_entries WHERE user_id=%s ORDER BY created_at DESC", (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows
