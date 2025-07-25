from exercicios_de_aprendizado.exercise_9 import smallest_multiple


def test_smallest_multiple_10() -> None:
    assert smallest_multiple(10) == 2_520


def test_smallest_multiple_20() -> None:
    assert smallest_multiple(20) == 232_792_560