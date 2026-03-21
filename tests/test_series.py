import pytest

from exercicios_de_aprendizado.series import slice


@pytest.mark.parametrize(
    "series, length, expected",
    [
        ("49142", 3, ["491", "914", "142"]),
        ("49142", 4, ["4914", "9142"]),
        ("49142", 5, ["49142"]),
        ("12345", 1, ["1", "2", "3", "4", "5"]),
        ("97867564", 2, ["97", "78", "86", "67", "75", "56", "64"]),
    ],
)
def test_slice_returns_correct_substrings(
    series: str,
    length: int,
    expected: list[str],
) -> None:
    assert slice(series, length) == expected


@pytest.mark.parametrize(
    "series, length, expected_error",
    [
        ("12345", 0, "slice length cannot be zero"),
        ("12345", -1, "slice length cannot be negative"),
        ("", 3, "series cannot be empty"),
        ("123", 6, "slice length cannot be greater than series length"),
    ],
)
def test_slice_raises_value_error(
    series: str,
    length: int,
    expected_error: str,
) -> None:
    with pytest.raises(ValueError, match=expected_error):
        slice(series, length)
