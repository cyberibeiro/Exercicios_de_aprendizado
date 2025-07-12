from exercicios_de_aprendizado.exercise_6 import *


def test_append():
    assert append([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concatenate():
    assert concatenate([1], [2, 3], [4]) == [1, 2, 3, 4]


def test_filter():
    assert filter(lambda x: x > 2, [1, 2, 3, 4]) == [3, 4]


def test_length():
    assert length([9, 8, 7]) == 3


def test_map():
    assert map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]


def test_foldl():
    assert foldl(lambda acc, x: acc - x, [1, 2, 3], 10) == 4


def test_foldr():
    assert foldr(lambda x, acc: acc - x, [1, 2, 3], 10) == 4


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


if __name__ == "__main__":
    test_append()
    test_concatenate()
    test_filter()
    test_length()
    test_map()
    test_foldl()
    test_foldr()
    test_reverse()
    print("✅ Todos os testes passaram!")
