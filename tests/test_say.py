from pytest import mark, raises

from exercicios_de_aprendizado.say import say


@mark.parametrize(
    "number, expected",
    [
        (0, "zero"),
        (1, "one"),
        (12, "twelve"),
        (123, "one hundred twenty three"),
        (1_000, "one thousand"),
        (1_234, "one thousand two hundred thirty four"),
        (1_000_000, "one million"),
        (1_000_001, "one million one"),
        (
            1_234_567,
            "one million two hundred thirty four thousand five hundred sixty seven",
        ),
        (1_000_000_000, "one billion"),
        (
            999_999_999_999,
            "nine hundred ninety nine billion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine",
        ),
        (
            987_654_321_123,
            "nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three",
        ),
    ],
)
def test_valid_numbers(number: int, expected: str) -> None:
    assert say(number) == expected


def test_out_of_range_negative() -> None:
    with raises(ValueError, match="input out of range"):
        say(-1)


def test_out_of_range_too_large() -> None:
    with raises(ValueError, match="input out of range"):
        say(1_000_000_000_000)        say(1_000_000_000_000)