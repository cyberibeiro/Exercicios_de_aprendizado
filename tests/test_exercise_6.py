from exercicios_de_aprendizado.exercise_6 import *


def test_append() -> None:
    assert append([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concatenate() -> None:
    assert concatenate([1], [2, 3], [4]) == [1, 2, 3, 4]


def test_filter() -> None:
    assert filter(lambda x: x > 2, [1, 2, 3, 4]) == [3, 4]


def test_length() -> None:
    assert length([9, 8, 7]) == 3
    assert length(["Ana", "Bruno", "Clara", "Daniel"]) == 4


def test_map() -> None:
    assert map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]


def test_foldl() -> None:
    assert foldl(lambda acc, x: x - acc, [1, 2, 3], 10) == -8


def test_foldr() -> None:
    assert foldr(lambda x, acc: acc - x, [1, 2, 3], 10) == 4


def test_reverse() -> None:
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
