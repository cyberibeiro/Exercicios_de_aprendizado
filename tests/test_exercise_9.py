from exercicios_de_aprendizado.exercise_9 import 


def test_on_earth() -> None:
    assert SpaceAge(1000000000).on_earth() == 31.69


def test_on_mercury() -> None:
    assert SpaceAge(2134835688).on_mercury() == 280.88


def test_on_venus() -> None:
    assert SpaceAge(189839836).on_venus() == 9.78


def test_on_mars() -> None:
    assert SpaceAge(2329871239).on_mars() == 39.25


def test_on_jupiter() -> None:
    assert SpaceAge(901876382).on_jupiter() == 2.41


def test_on_saturn() -> None:
    assert SpaceAge(3000000000).on_saturn() == 3.23


def test_on_uranus() -> None:
    assert SpaceAge(3210123456).on_uranus() == 1.21


def test_on_neptune() -> None:
    assert SpaceAge(8210123456).on_neptune() == 1.58
    assert SpaceAge(8210123456).on_neptune() == 1.58
