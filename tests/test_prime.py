import pytest

from exercicios_de_aprendizado.prime import is_prime, nth_prime


@pytest.mark.parametrize(
    "number, expected",
    [
        (-5, False),
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (9, False),
        (101, True),
        (997, True),
    ],
)
def test_is_prime(number: int, expected: bool) -> None:
    assert is_prime(number) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (5, 11),
        (10_001, 104743),
    ],
)
def test_nth_prime_values(n: int, expected: int) -> None:
    """Testa se nth_prime retorna o n-ésimo primo correto e garante que é realmente primo."""
    result = nth_prime(n)
    assert result == expected
    assert is_prime(result)


@pytest.mark.parametrize(
    "invalid_n",
    [0, -1, -10],
)
def test_nth_prime_invalid(invalid_n: int) -> None:
    """Testa se nth_prime lança ValueError para entradas inválidas (n <= 0)."""
    with pytest.raises(ValueError):
        nth_prime(invalid_n)

        nth_prime(invalid_n)
