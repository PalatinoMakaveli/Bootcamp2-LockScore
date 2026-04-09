from src.password_checker import check_password_strength

# Caminho feliz
def test_senha_forte():
    assert check_password_strength("Abc123@SenhaForte") == "Forte"

# Entrada fraca
def test_senha_fraca():
    assert check_password_strength("123") == "Fraca"

# Caso intermediário
def test_senha_media():
    assert check_password_strength("abc123ABC") == "Média"

# Caso inválido (extra — te dá mais ponto)
def test_senha_vazia():
    assert check_password_strength("") == "Fraca"