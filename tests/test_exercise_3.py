from src.exercicios_de_aprendizado.exercise_3 import exercise_3


def test_com_dez() -> None:
    assert exercise_3(10) == 10


def test_com_mais() -> None:
    assert exercise_3(4_000_000) == 4613732
