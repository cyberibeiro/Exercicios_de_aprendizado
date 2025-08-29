from exercicios_de_aprendizado.rational_numbers import Rational_Numbers

def test_rational_basic() -> None:
    assert Rational_Numbers(2, 4) == Rational_Numbers(1, 2)
    assert Rational_Numbers(-2, -4) == Rational_Numbers(1, 2)
    assert Rational_Numbers(3, -6) == Rational_Numbers(-1, 2)

def test_operations() -> None:
    a, b = Rational_Numbers(1, 2), Rational_Numbers(1, 3)
    assert a + b == Rational_Numbers(5, 6)
    assert a - b == Rational_Numbers(1, 6)
    assert a * b == Rational_Numbers(1, 6)
    assert a / b == Rational_Numbers(3, 2)

def test_abs() -> None:
    assert abs(Rational_Numbers(-1, 2)) == Rational_Numbers(1, 2)
    assert abs(Rational_Numbers(1, -2)) == Rational_Numbers(1, 2)

def test_pow_int() -> None:
    r = Rational_Numbers(2, 3)
    assert r.pow_int(2) == Rational_Numbers(4, 9)
    assert r.pow_int(-2) == Rational_Numbers(9, 4)

def test_pow_real() -> None:
    r = Rational_Numbers(4, 9)
    assert abs(r.pow_real(0.5) - (2/3)) < 1e-9

def test_real_pow_rational() -> None:
    r = Rational_Numbers(1, 2)
    assert abs(r.real_pow_rational(9) - 3.0) < 1e-9 
