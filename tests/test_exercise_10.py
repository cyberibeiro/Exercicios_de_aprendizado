from datetime import datetime
from exercicios_de_aprendizado.exercise_10 import Gigasecond

def test_date_exact_gigasecond() -> None:
    start = datetime(2015, 1, 24, 22, 0, 0)
    expected = datetime(2046, 10, 2, 23, 46, 40)
    assert Gigasecond(start).date() == expected
          #Cria objeto      #Usa o método
def test_date_only_date_given() -> None:
    start = datetime(2000, 1, 1)
    expected = datetime(2031, 9, 9, 1, 46, 40)
    assert Gigasecond(start).date() == expected

def test_recent_date() -> None:
    start = datetime(2023, 7, 30, 15, 30, 0)
    expected = datetime(2055, 4, 7, 17, 16, 40)
    assert Gigasecond(start).date() == expected
