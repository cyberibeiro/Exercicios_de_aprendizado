import pytest

from exercicios_de_aprendizado.prime_factors import prime_factorization


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (9, [3, 3]),
        (12, [2, 2, 3]),
        (84, [2, 2, 3, 7]),
        (360, [2, 2, 2, 3, 3, 5]),
        (97, [97]),
        (1001, [7, 11, 13]),
        (1024, [2] * 10),
        (999983, [999983]),
        (10**6, [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]),
        (10**9, [2] * 9 + [5] * 9),
        (9999999967, [9999999967]),
        (600851475143, [71, 839, 1471, 6857]),
        (999999000001, [999999000001]),
        (2**20 * 3**5 * 7**2, [2] * 20 + [3] * 5 + [7] * 2),
        (99999999977, [99999999977]),
        (1234567890, [2, 3, 3, 5, 3607, 3803]),
    ],
)
def test_prime_factorization_valid_inputs(number, expected) -> None:
    """Testa fatorações conhecidas, incluindo números grandes e primos."""
    assert prime_factorization(number) == expected


@pytest.mark.parametrize("invalid_input", [0, -1, -100, 3.14, "abc", None])
def test_prime_factorization_invalid_inputs(invalid_input) -> None:
    """Testa entradas inválidas e tipos incorretos."""
    with pytest.raises(ValueError):
        prime_factorization(invalid_input)
        prime_factorization(invalid_input)
