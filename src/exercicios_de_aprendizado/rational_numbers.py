from __future__ import annotations

from math import gcd
from multiprocessing import Value
from typing import Any


class Rational_Numbers:
    def __init__(
        self,
        numerador: int,
        denominador: int,
    ) -> None:
        """
        Inicializa um número racional reduzido.

        Args:
            num (int): Numerador.
            den (int): Denominador (não pode ser zero).

        Raises:
            ValueError: Se o denominador for zero.
        """
        if denominador == 0:
            raise ValueError("Denominador não pode ser zero.")
        if denominador < 0:
            numerador, denominador = -numerador, -denominador
        g = gcd(numerador, denominador)
        self.numerador, self.denominador = numerador // g, denominador // g

    def __repr__(self) -> str:
        """
        Retorna a representação textual da fração.

        Returns:
            str: Representação no formato 'Rational(num, den)'.
        """
        return f"Rational({self.numerador}, {self.denominador})"

    def __eq__(self, other: Any) -> bool:
        """
        Verifica se dois números racionais são iguais.

        Args:
            other (object): Outro objeto a ser comparado.

        Returns:
            bool: True se forem ambos Rational e iguais, False caso contrário.
        """
        if isinstance(other, Rational_Numbers):
            return (self.numerador, self.denominador) == (
                other.numerador,
                other.denominador,
            )

        raise ValueError(f"Comparison cannot have class: {type(other)}")

    def __add__(self, other: Rational_Numbers) -> Rational_Numbers:
        """
        Soma dois números racionais.

        Args:
            other (Rational): Outro número racional.

        Returns:
            Rational: Resultado da soma.
        """
        return Rational_Numbers(
            self.numerador * other.denominador + other.numerador * self.denominador,
            self.denominador * other.denominador,
        )

    def __sub__(self, other: Rational_Numbers) -> Rational_Numbers:
        """
        Subtrai outro número racional deste.

        Args:
            other (Rational): Outro número racional.

        Returns:
            Rational: Resultado da subtração.
        """
        return Rational_Numbers(
            self.numerador * other.denominador - other.numerador * self.denominador,
            self.denominador * other.denominador,
        )

    def __mul__(self, other: Rational_Numbers) -> Rational_Numbers:
        """
        Multiplica dois números racionais.

        Args:
            other (Rational): Outro número racional.

        Returns:
            Rational: Resultado da multiplicação.
        """
        return Rational_Numbers(
            self.numerador * other.numerador, self.denominador * other.denominador
        )

    def __truediv__(self, other: Rational_Numbers) -> Rational_Numbers:
        """
        Divide este número racional por outro.

        Args:
            other (Rational): Outro número racional.

        Raises:
            ZeroDivisionError: Se o numerador do outro for zero.

        Returns:
            Rational: Resultado da divisão.
        """
        if other.numerador == 0:
            raise ZeroDivisionError("Divisão por zero")
        return Rational_Numbers(
            self.numerador * other.denominador, self.denominador * other.numerador
        )

    def __abs__(self) -> Rational_Numbers:
        """
        Retorna o valor absoluto do número racional.

        Returns:
            Rational: Fração com numerador positivo.
        """
        return Rational_Numbers(abs(self.numerador), self.denominador)

    def pow_int(self, n: int) -> Rational_Numbers:
        """
        Eleva o número racional a uma potência inteira.

        Args:
            n (int): Expoente inteiro.

        Returns:
            Rational: Resultado da potência.
        """
        if n >= 0:
            return Rational_Numbers(self.numerador**n, self.denominador**n)
        else:
            return Rational_Numbers(self.denominador**-n, self.numerador**-n)

    def pow_real(self, x: float) -> float:
        """
        Eleva o número racional a uma potência real.

        Args:
            x (float): Expoente real.

        Returns:
            float: Resultado da potência.
        """
        return (self.numerador**x) / (self.denominador**x)

    def real_pow_rational(self, x: float) -> float:
        """
        Eleva um número real a este número racional.

        Args:
            x (float): Número real.

        Returns:
            float: Resultado de x^(num/den).
        """
        return x ** (self.numerador / self.denominador)
