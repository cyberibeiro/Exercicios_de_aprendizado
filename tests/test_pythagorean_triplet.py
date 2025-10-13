import pytest

from pythagorean_triplet import find_pythagorean_triplet


@pytest.mark.parametrize(
    "total_sum, expected_product",
    [
        (12, 60),
        (30, 780),
        (1000, 31875000),  # Project Euler
    ],
)
def test_find_special_pythagorean_triplet(
    total_sum: int, expected_product: int
) -> None:

    result = find_pythagorean_triplet(total_sum)

    assert result is not None, "Expected a valid Pythagorean triplet, but got None"

    a, b, c, product = result

    assert a**2 + b**2 == c**2, "Does not satisfy the Pythagorean theorem"
    assert a + b + c == total_sum, "Sum of sides does not match total_sum"
    assert product == expected_product, "Incorrect product for the given total_sum"
    assert product == expected_product, "Incorrect product for the given total_sum"
