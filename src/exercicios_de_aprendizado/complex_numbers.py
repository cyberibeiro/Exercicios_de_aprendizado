import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.imag * other.real + self.real * other.imag
        )

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom
        )

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def exp(self):
        exp_a = math.exp(self.real)
        return Complex(exp_a * math.cos(self.imag), exp_a * math.sin(self.imag))

    # --- extras para facilitar testes ---
    def __eq__(self, other):
        """Permite comparação direta com =="""
        return (
            math.isclose(self.real, other.real, rel_tol=1e-9, abs_tol=1e-9)
            and math.isclose(self.imag, other.imag, rel_tol=1e-9, abs_tol=1e-9)
        )

    def __repr__(self):
        """Representação útil em erros de teste"""
        return f"Complex({self.real}, {self.imag})"
