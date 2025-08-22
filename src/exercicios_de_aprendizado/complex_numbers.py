from __future__ import annotations

from math import cos, exp, isclose, sin, sqrt


class Complex_numbers:
    def __init__(
        self,
        real: float,
        imag: float,
    ) -> None:
        """
        Inicializa um número complexo no formato (a + bi).

        Args:
            real (float): parte real do número complexo.
            imag (float): parte imaginária do número complexo.
        """
        self.real = real
        self.imag = imag

    def __add__(self, other: Complex_numbers) -> Complex_numbers:
        """
        Soma dois números complexos.

        Fórmula:
            (a + bi) + (c + di) = (a + c) + (b + d)i

        Args:
            other (Complex_numbers): outro número complexo.

        Returns:
            Complex_numbers: resultado da soma.
        """
        return Complex_numbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: Complex_numbers) -> Complex_numbers:
        """
        Subtrai dois números complexos.

        Fórmula:
            (a + bi) - (c + di) = (a - c) + (b - d)i

        Args:
            other (Complex_numbers): outro número complexo.

        Returns:
            Complex_numbers: resultado da subtração.
        """
        return Complex_numbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: Complex_numbers) -> Complex_numbers:
        """
        Multiplica dois números complexos.

        Fórmula:
            (a + bi) * (c + di) = (ac - bd) + (ad + bc)i

        Args:
            other (Complex_numbers): outro número complexo.

        Returns:
            Complex_numbers: resultado da multiplicação.
        """
        return Complex_numbers(
            self.real * other.real - self.imag * other.imag,
            self.imag * other.real + self.real * other.imag,
        )

    def __truediv__(self, other: Complex_numbers) -> Complex_numbers:
        """
        Divide dois números complexos.

        Fórmula:
            (a + bi) / (c + di) = [(ac + bd) / (c² + d²)] + [(bc - ad) / (c² + d²)]i

        Args:
            other (Complex_numbers): outro número complexo (divisor).

        Returns:
            Complex_numbers: resultado da divisão.
        """
        denom = other.real**2 + other.imag**2
        return Complex_numbers(
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom,
        )

    def conjugate(self) -> Complex_numbers:
        """
        Retorna o conjugado de um número complexo.

        Fórmula:
            conj(a + bi) = a - bi

        Returns:
            Complex_numbers: número complexo conjugado.
        """
        return Complex_numbers(self.real, -self.imag)

    def abs(self) -> float:
        """
        Retorna o valor absoluto (módulo) de um número complexo.

        Fórmula:
            |a + bi| = √(a² + b²)

        Returns:
            float: valor absoluto (sempre ≥ 0).
        """
        return sqrt(self.real**2 + self.imag**2)

    def exp(self) -> Complex_numbers:
        """
        Calcula a exponencial de um número complexo usando a fórmula de Euler.

        Fórmula:
            e^(a+bi) = e^a * (cos(b) + i·sin(b))

        Returns:
            Complex_numbers: resultado da exponencial.
        """
        exp_a = exp(self.real)
        return Complex_numbers(exp_a * cos(self.imag), exp_a * sin(self.imag))

    def __eq__(self, other: object) -> bool:
        """
        Compara dois números complexos para verificar se são aproximadamente iguais.

        Args:
            other (object): outro número complexo.

        Returns:
            bool: True se forem (quase) iguais, False caso contrário.
        """
        return (
            isinstance(other, Complex_numbers)
            and isclose(self.real, other.real, rel_tol=1e-9, abs_tol=1e-9)
            and isclose(self.imag, other.imag, rel_tol=1e-9, abs_tol=1e-9)
        )

    def __repr__(self) -> str:
        """
        Representação em string de um número complexo.

        Returns:
            str: representação no formato 'Complex_numbers(a, b)'.
        """
        return f"Complex_numbers({self.real}, {self.imag})"
