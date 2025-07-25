import pytest

from src.exercicios_de_aprendizado.exercise_8 import SpaceAge


def test_on_earth() -> None:
    assert SpaceAge(1_000_000_000).on_planet("earth") == 31.69


def test_on_mercury() -> None:
    assert SpaceAge(2_134_835_688).on_planet("mercury") == 280.88


def test_on_venus() -> None:
    assert SpaceAge(189_839_836).on_planet("venus") == 9.78


def test_on_mars() -> None:
    assert SpaceAge(2_329_871_239).on_planet("mars") == 39.25


def test_on_jupiter() -> None:
    assert SpaceAge(901_876_382).on_planet("jupiter") == 2.41


def test_on_saturn() -> None:
    assert SpaceAge(3_000_000_000).on_planet("saturn") == 3.23


def test_on_uranus() -> None:
    assert SpaceAge(3_210_123_456).on_planet("uranus") == 1.21


def test_on_neptune() -> None:
    assert SpaceAge(8_210_123_456).on_planet("neptune") == 1.58


def test_on_invalid_planet_raises_error() -> None:
    age_calculator = SpaceAge(1_000_000_000)
    with pytest.raises(ValueError) as excinfo:
        age_calculator.on_planet("plutao")
    assert "Planeta 'plutao' não encontrado." in str(excinfo.value)
