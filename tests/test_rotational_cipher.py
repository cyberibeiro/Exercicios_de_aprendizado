from exercicios_de_aprendizado.rotational_cipher import RotationalCipher

def test_encrypt_lowercase() -> None:
    assert RotationalCipher("abcdefghijklmnopqrstuvwxyz", 13).encrypt() == "nopqrstuvwxyzabcdefghijklm"

def test_encrypt_uppercase() -> None:
    assert RotationalCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 13).encrypt() == "NOPQRSTUVWXYZABCDEFGHIJKLM"

def test_encrypt_with_mixed_case() -> None:
    assert RotationalCipher("Beatriz", 3).encrypt() == "Ehdwulc"

def test_encrypt_with_special_chars() -> None:
    assert RotationalCipher("Yasmim", 5).encrypt() == "Dfxrnr"

def test_decrypt_lowercase() -> None:
    assert RotationalCipher("nopqrstuvwxyzabcdefghijklm", 13).decrypt() == "abcdefghijklmnopqrstuvwxyz"

def test_decrypt_uppercase() -> None:
    assert RotationalCipher("NOPQRSTUVWXYZABCDEFGHIJKLM", 13).decrypt() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def test_decrypt_with_mixed_case() -> None:
    assert RotationalCipher("Ehdwulc", 3).decrypt() == "Beatriz"

def test_decrypt_with_special_chars() -> None:
    assert RotationalCipher("Dfxrnr", 5).decrypt() == "Yasmim"