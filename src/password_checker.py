import re

def check_password_strength(password: str) -> str:
    score = 0

    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@#$%&]", password):
        score += 1

    if score <= 2:
        return "Fraca"
    elif score <= 4:
        return "Média"
    else:
        return "Forte"