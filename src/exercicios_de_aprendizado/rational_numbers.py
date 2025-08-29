from __future__ import annotations
from math import gcd

class Rational_Numbers:
    def __init__(self, num: int, den: int) -> None:
        """
        Inicializa um número racional reduzido.

        Args:
            num (int): Numerador.
            den (int): Denominador (não pode ser zero).

        Raises:
            ValueError: Se o denominador for zero.
        """
        if den == 0:
            raise ValueError("Denominador não pode ser zero.")
        if den < 0:
            num, den = -num, -den
        g = gcd(num, den)
        self.num, self.den = num // g, den // g

    def __repr__(self) -> str:
        """
        Retorna a representação textual da fração.

        Returns:
            str: Representação no formato 'Rational(num, den)'.
        """
        return f"Rational({self.num}, {self.den})"

    def __eq__(self, other: object) -> bool:
        """
        Verifica se dois números racionais são iguais.

        Args:
            other (object): Outro objeto a ser comparado.

        Returns:
            bool: True se forem ambos Rational e iguais, False caso contrário.
        """
        return isinstance(other, Rational_Numbers) and (self.num, self.den) == (other.num, other.den)

    def __add__(self, other: Rational_Numbers) -> Rational_Numbers:
        """
        Soma dois números racionais.

        Args:
            other (Rational): Outro número racional.

        Returns:
            Rational: Resultado da soma.
        """
        return Rational_Numbers(self.num * other.den + other.num * self.den, self.den * other.den)

    def __sub__(self, other: Rational_Numbers) -> Rational_Numbers:
        """
        Subtrai outro número racional deste.

        Args:
            other (Rational): Outro número racional.

        Returns:
            Rational: Resultado da subtração.
        """
        return Rational_Numbers(self.num * other.den - other.num * self.den, self.den * other.den)

    def __mul__(self, other: Rational_Numbers) -> Rational_Numbers:
        """
        Multiplica dois números racionais.

        Args:
            other (Rational): Outro número racional.

        Returns:
            Rational: Resultado da multiplicação.
        """
        return Rational_Numbers(self.num * other.num, self.den * other.den)

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
        if other.num == 0:
            raise ZeroDivisionError("Divisão por zero")
        return Rational_Numbers(self.num * other.den, self.den * other.num)

    def __abs__(self) -> Rational_Numbers:
        """
        Retorna o valor absoluto do número racional.

        Returns:
            Rational: Fração com numerador positivo.
        """
        return Rational_Numbers(abs(self.num), self.den)

    def pow_int(self, n: int) -> Rational_Numbers:
        """
        Eleva o número racional a uma potência inteira.

        Args:
            n (int): Expoente inteiro.

        Returns:
            Rational: Resultado da potência.
        """
        if n >= 0:
            return Rational_Numbers(self.num**n, self.den**n)
        else:
            return Rational_Numbers(self.den**-n, self.num**-n)

    def pow_real(self, x: float) -> float:
        """
        Eleva o número racional a uma potência real.

        Args:
            x (float): Expoente real.

        Returns:
            float: Resultado da potência.
        """
        return (self.num ** x) / (self.den ** x)

    def real_pow_rational(self, x: float) -> float:
        """
        Eleva um número real a este número racional.

        Args:
            x (float): Número real.

        Returns:
            float: Resultado de x^(num/den).
        """
        return x ** (self.num / self.den)
