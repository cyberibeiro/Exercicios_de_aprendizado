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
        (1_001, [7, 11, 13]),
        (1_024, [2] * 10),
        (999_983, [999_983]),
        (10**6, [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]),
        (10**9, [2] * 9 + [5] * 9),
        (9_999_999_967, [9_999_999_967]),
        (600_851_475_143, [71, 839, 1_471, 6_857]),
        (999_999_000_001, [999_999_000_001]),
        (2**20 * 3**5 * 7**2, [2] * 20 + [3] * 5 + [7] * 2),
        (99_999_999_977, [99_999_999_977]),
        (12_345_678_90, [2, 3, 3, 5, 3_607, 3_803]),
    ],
)
def test_prime_factorization_valid_inputs(number, expected) -> None:
    """Testa fatorações conhecidas, incluindo números grandes e primos."""
    assert prime_factorization(number) == expected


@pytest.mark.parametrize("invalid_input", [0, -1, -100])
def test_prime_factorization_invalid_inputs(invalid_input) -> None:
    """Testa entradas inválidas e tipos incorretos."""
    with pytest.raises(ValueError):
        prime_factorization(invalid_input)
