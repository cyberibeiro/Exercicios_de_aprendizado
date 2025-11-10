import pytest

from exercicios_de_aprendizado.summation_of_primes import sum_primes_below


@pytest.mark.parametrize(
    "limit, expected_sum",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 2),
        (10, 17),
        (20, 77),
        (100, 1_060),
        (2_000_000, 142_913_828_922),
    ],
)
def test_sum_primes_below(limit: int, expected_sum: int) -> None:
    result = sum_primes_below(limit)
    assert result == expected_sum
