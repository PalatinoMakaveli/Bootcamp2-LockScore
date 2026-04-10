from src.password_checker import check_password_strength

def test_senha_forte():
    assert check_password_strength("Abc123@SenhaForte")["strength"] == "Forte"

def test_senha_fraca():
    assert check_password_strength("123")["strength"] == "Fraca"

def test_senha_media():
    assert check_password_strength("abc123ABC")["strength"] == "Média"

def test_senha_vazia():
    assert check_password_strength("")["strength"] == "Fraca"