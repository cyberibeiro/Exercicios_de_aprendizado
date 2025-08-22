from exercicios_de_aprendizado.complex_numbers import Complex

def test_addition() -> None:
    assert Complex(1, 2) + Complex(3, 4) == Complex(4, 6)

def test_subtraction() -> None:
    assert Complex(5, 7) - Complex(2, 3) == Complex(3, 4)

def test_multiplication() -> None:
    assert Complex(1, 2) * Complex(3, 4) == Complex(-5, 10)

def test_division() -> None:
    assert Complex(1, 2) / Complex(3, 4) == Complex(0.44, 0.08)

def test_conjugate() -> None:
    assert Complex(3, 4).conjugate() == Complex(3, -4)

def test_abs() -> None:
    assert Complex(3, 4).abs() == 5.0

def test_exp() -> None:
    result = Complex(0, 3.141592653589793).exp()
    assert result == Complex(-1.0, 0.0)