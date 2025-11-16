# Exercism - Say: https://exercism.org/tracks/python/exercises/say

NUMBER_WORDS_0_TO_19 = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

TENS_WORDS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

SCALE_GROUPS = [
    (10**9, "billion"),
    (10**6, "million"),
    (10**3, "thousand"),
    (1, ""),
]


def convert_three_digits_to_words(three_digit_number: int) -> str:
    """
    Converte um número entre 0 e 999 em palavras.
    Não aplica escala (mil, milhão etc.).
    """
    words: list[str] = []

    hundreds_value, remainder = divmod(three_digit_number, 100)

    if hundreds_value:
        words.append(NUMBER_WORDS_0_TO_19[hundreds_value])
        words.append("hundred")

    if remainder:
        if remainder < 20:
            words.append(NUMBER_WORDS_0_TO_19[remainder])
        else:
            tens_value, ones_value = divmod(remainder, 10)
            words.append(TENS_WORDS[tens_value])
            if ones_value:
                words.append(NUMBER_WORDS_0_TO_19[ones_value])

    return " ".join(words)


def say(number: int) -> str:
    """
    Converte um número inteiro entre 0 e 999 999 999 999
    para sua forma por extenso em inglês.
    """
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    if number < 1000:
        return convert_three_digits_to_words(number)

    words: list[str] = []

    for scale_value, scale_name in SCALE_GROUPS:
        if scale_value > 1 and number >= scale_value:
            group_value = number // scale_value
            number = number % scale_value

            group_words = convert_three_digits_to_words(group_value)
            words.append(group_words)

            if scale_name:
                words.append(scale_name)

        elif scale_value == 1 and number > 0:
            words.append(convert_three_digits_to_words(number))
            number = 0

    return " ".join(words).strip()