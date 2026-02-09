import pytest

from exercicios_de_aprendizado.acronym import generate_acronym


@pytest.mark.parametrize(
    "phrase, expected",
    [
        ("As Soon As Possible", "ASAP"),
        ("Liquid-crystal display", "LCD"),
        ("Thank George It's Friday!", "TGIF"),
        ("random Access Memory", "RAM"),
        ("Complementary metal-oxide semiconductor", "CMOS"),
        ("Word", "W"),
        ("Portable Network Graphics", "PNG"),
        ("Ruby on Rails", "ROR"),
        ("First In, First Out", "FIFO"),
        ("Self-contained underwater breathing apparatus", "SCUBA"),
        ("First In, First Out!", "FIFO"),
        ("Wait, What?", "WW"),
        ("This. Has. Dots.", "THD"),
        ("Don't Repeat Yourself", "DRY"),
        ("Rock 'n' Roll", "RNR"),
        ("It's a Trap!", "IAT"),
        ("random access memory", "RAM"),
        ("RaNdOm AcCeSs MeMoRy", "RAM"),
        ("PYTHON enhancement proposal", "PEP"),
        ("", ""),
        ("123 456", ""),
        ("!!! ???", ""),
        ("One", "O"),
        ("X", "X"),
    ],
)
def test_generate_acronym(phrase: str, expected: str) -> None:
    assert generate_acronym(phrase) == expected
    assert generate_acronym(phrase) == expected
