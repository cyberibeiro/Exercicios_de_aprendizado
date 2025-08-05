from exercicios_de_aprendizado.rotational_cipher import caesar_cipher

def test_caesar_cipher_13() -> None:
    assert caesar_cipher("abcdefghijklmnopqrstuvwxyz", 13) == "nopqrstuvwxyzabcdefghijklm"

def test_caesar_cipher_3() -> None:
    assert caesar_cipher("abc", 3) == "def"

def test_caesar_cipher_3_maiuscula() -> None:
    assert caesar_cipher("Beatriz", 3) == "Endwulc"