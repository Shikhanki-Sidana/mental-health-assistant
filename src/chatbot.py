import re
from db import get_connection

SUICIDAL_PATTERNS = [r"suicid", r"kill myself", r"want to die", r"end my life"]

def contains_suicidal_thoughts(text):
    return any(re.search(p, text.lower()) for p in SUICIDAL_PATTERNS)

def bot_reply(user_id, text):
    if contains_suicidal_thoughts(text):
        return "If you're thinking about harming yourself, please call 988 (US) or your local emergency number immediately."
    if 'anx' in text.lower():
        return "Try deep breathing, grounding exercises, and short walks. Persistent anxiety may need professional care."
    return "I'm here to listen. Tell me more or type 'screen' to take a questionnaire."
