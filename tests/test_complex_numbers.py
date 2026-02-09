from exercicios_de_aprendizado.complex_numbers import Complex_numbers


def test_addition() -> None:
    assert Complex_numbers(1, 2) + Complex_numbers(3, 4) == Complex_numbers(4, 6)


def test_subtraction() -> None:
    assert Complex_numbers(5, 7) - Complex_numbers(2, 3) == Complex_numbers(3, 4)


def test_multiplication() -> None:
    assert Complex_numbers(1, 2) * Complex_numbers(3, 4) == Complex_numbers(-5, 10)


def test_division() -> None:
    assert Complex_numbers(1, 2) / Complex_numbers(3, 4) == Complex_numbers(0.44, 0.08)


def test_conjugate() -> None:
    assert Complex_numbers(3, 4).conjugate() == Complex_numbers(3, -4)


def test_abs() -> None:
    assert Complex_numbers(3, 4).abs() == 5.0


def test_exp() -> None:
    result = Complex_numbers(0, 3.141592653589793).exp()
    assert result == Complex_numbers(-1.0, 0.0)


def test_repr() -> None:
    z = Complex_numbers(3, -4)
    assert repr(z) == "Complex_numbers(3, -4)"
    assert repr(z) == "Complex_numbers(3, -4)"
