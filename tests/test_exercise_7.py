from exercicios_de_aprendizado.exercise_7 import find_the_largest_palindrome

def test_example() -> None:
    assert find_the_largest_palindrome(10,99) == 9009

def test_exercise() -> None:
    assert find_the_largest_palindrome(100, 999) == 906609