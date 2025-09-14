

import pytest
from exercicios_de_aprendizado.prime import is_prime, nth_prime

@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, True),
        (5, True),
        (1, False),
        (4, False),
        (9, False),
    ],
)
def test_is_prime(number: int, expected: bool) -> None:
    assert is_prime(number) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),      # 1º primo
        (2, 3),      # 2º primo
        (3, 5),      # 3º primo
        (5, 11),     # 5º primo
        (10_001, 104743),  # 10001º primo
    ],
)
def test_nth_prime(n: int, expected: int) -> None:
    assert nth_prime(n) == expected