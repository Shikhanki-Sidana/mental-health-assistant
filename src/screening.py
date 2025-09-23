import json
from db import get_connection

def score_phq9(answers):
    s = sum(int(a) for a in answers[:9])
    if s >= 20: cat = "Severe depression"
    elif s >=15: cat = "Moderately severe"
    elif s >=10: cat = "Moderate"
    elif s >=5: cat = "Mild"
    else: cat = "None-minimal"
    return s, cat

def save_screening(user_id, tool, score, answers):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO screenings (user_id,tool,score,raw_answers) VALUES (%s,%s,%s,%s)",
                (user_id,tool,score,json.dumps(answers)))
    conn.commit()
    conn.close()
