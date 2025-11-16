import pytest

from exercicios_de_aprendizado.say import say

@pytest.mark.parametrize("number, expected", [
    (0, "zero"),
    (1, "one"),
    (12, "twelve"),
    (123, "one hundred twenty three"),
    (1_000, "one thousand"),
    (1_234, "one thousand two hundred thirty four"),
    (1_000_000, "one million"),
    (1_000_001, "one million one"),
    (1_234_567, "one million two hundred thirty four thousand five hundred sixty seven"),
    (1_000_000_000, "one billion"),
    (999_999_999_999, "nine hundred ninety nine billion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine"),
])
def test_valid_numbers(number : int, expected : str) -> None:
    assert say(number) == expected

def test_out_of_range_negative() -> None:
    with pytest.raises(ValueError) as error_message:
        say(-1)
    assert str(error_message.value) == "input out of range"

def test_out_of_range_too_large() -> None:
    with pytest.raises(ValueError) as error_message:
        say(1_000_000_000_000)
    assert str(error_message.value) == "input out of range"