from exercicios_de_aprendizado.exercise_1 import exercise_1

def test_example() -> None:
    assert exercise_1(10) == 23

def test_exercise() -> None:
    assert exercise_1(1_000) == 233_168