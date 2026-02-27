import pytest

from exercicios_de_aprendizado.highly_divisible_triangular_number import (
    count_divisors,
    first_triangular_with_more_than_n_divisors,
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (-1, 0),  # negativo
        (0, 0),
        (1, 1),
        (6, 4),
        (28, 6),
        (36, 9),  # quadrado perfeito
    ],
)
def test_count_divisors(n: int, expected: int) -> None:
    result = count_divisors(n)
    assert result == expected


@pytest.mark.parametrize(
    "min_divisors, expected",
    [
        (1, 3),
        (2, 6),
        (4, 28),
        (5, 28),
        (500, 76_576_500),
    ],
)
def test_first_triangular_with_more_than_n_divisors(
    min_divisors: int, expected: int
) -> None:
    result = first_triangular_with_more_than_n_divisors(min_divisors)
    assert result == expected
