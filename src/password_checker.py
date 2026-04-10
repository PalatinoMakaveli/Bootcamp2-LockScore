import re

def check_password_strength(password: str):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use pelo menos 12 caracteres")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Adicione letras maiúsculas")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Adicione letras minúsculas")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Adicione números")

    if re.search(r"[@#$%&]", password):
        score += 1
    else:
        feedback.append("Adicione caracteres especiais (@#$%&)")

    # Classificação + barra
    if score <= 2:
        strength = "Fraca"
        color = "red"
        time = "Pode ser quebrada em segundos"
        width = "30%"
    elif score <= 4:
        strength = "Média"
        color = "orange"
        time = "Pode levar algumas horas ou dias"
        width = "60%"
    else:
        strength = "Forte"
        color = "green"
        time = "Pode levar anos para ser quebrada"
        width = "100%"

    return {
        "strength": strength,
        "color": color,
        "time": time,
        "feedback": feedback,
        "width": width
    }