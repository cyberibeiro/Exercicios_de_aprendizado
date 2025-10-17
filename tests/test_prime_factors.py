import pytest
from exercicios_de_aprendizado.prime_factors import prime_factors


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (12, [2, 2, 3]),
        (60, [2, 2, 3, 5]),
        (13, [13]),
        (101, [101]),
        (9389, [41, 229]),
        (4745325, [3, 5, 5, 13, 31, 157]),
        (901255, [5, 17, 23, 461]),
        (1000000, [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]),
        (999999999989, [999999999989]),
        (97, [97]),
        (101, [101]),
        (103, [103]),
        (107, [107]),
        (109, [109]),
        (113, [113]),
        (1009, [1009]),
        (7919, [7919]),
        (104729, [104729]),
    ],
)
def test_prime_factorization(number: int, expected: list[int]) -> None:
    assert prime_factors(number) == expected