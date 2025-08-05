from exercicios_de_aprendizado.rotational_cipher import caesar_cipher

def test_caesar_cipher() -> None:
    assert caesar_cipher("abcdefghijklmnopqrstuvwxyz", 13) == "nopqrstuvwxyzabcdefghijklm"