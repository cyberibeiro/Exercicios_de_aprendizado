import math

class Complex:
    def __init__(self, real: float, imag: float) -> None:
        """
        Inicializa um número complexo no formato (a + bi).

        Args:
            real (float): parte real do número complexo.
            imag (float): parte imaginária do número complexo.
        """
        self.real = real
        self.imag = imag

    def __add__(self, other: "Complex") -> "Complex":
        """
        Soma dois números complexos.

        Fórmula:
            (a + bi) + (c + di) = (a + c) + (b + d)i

        Args:
            other (Complex): outro número complexo.

        Returns:
            Complex: resultado da soma.
        """
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: "Complex") -> "Complex":
        """
        Subtrai dois números complexos.

        Fórmula:
            (a + bi) - (c + di) = (a - c) + (b - d)i

        Args:
            other (Complex): outro número complexo.

        Returns:
            Complex: resultado da subtração.
        """
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: "Complex") -> "Complex":
        """
        Multiplica dois números complexos.

        Fórmula:
            (a + bi) * (c + di) = (ac - bd) + (ad + bc)i

        Args:
            other (Complex): outro número complexo.

        Returns:
            Complex: resultado da multiplicação.
        """
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.imag * other.real + self.real * other.imag
        )

    def __truediv__(self, other: "Complex") -> "Complex":
        """
        Divide dois números complexos.

        Fórmula:
            (a + bi) / (c + di) = [(ac + bd) / (c² + d²)] + [(bc - ad) / (c² + d²)]i

        Args:
            other (Complex): outro número complexo (divisor).

        Returns:
            Complex: resultado da divisão.
        """
        denom = other.real**2 + other.imag**2
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom
        )

    def conjugate(self) -> "Complex":
        """
        Retorna o conjugado de um número complexo.

        Fórmula:
            conj(a + bi) = a - bi

        Returns:
            Complex: número complexo conjugado.
        """
        return Complex(self.real, -self.imag)

    def abs(self) -> float:
        """
        Retorna o valor absoluto (módulo) de um número complexo.

        Fórmula:
            |a + bi| = √(a² + b²)

        Returns:
            float: valor absoluto (sempre ≥ 0).
        """
        return math.sqrt(self.real**2 + self.imag**2)

    def exp(self) -> "Complex":
        """
        Calcula a exponencial de um número complexo usando a fórmula de Euler.

        Fórmula:
            e^(a+bi) = e^a * (cos(b) + i·sin(b))

        Returns:
            Complex: resultado da exponencial.
        """
        exp_a = math.exp(self.real)
        return Complex(exp_a * math.cos(self.imag), exp_a * math.sin(self.imag))

    def __eq__(self, other: object) -> bool:
        """
        Compara dois números complexos para verificar se são aproximadamente iguais.

        Args:
            other (object): outro número complexo.

        Returns:
            bool: True se forem (quase) iguais, False caso contrário.
        """
        return (
            isinstance(other, Complex)
            and math.isclose(self.real, other.real, rel_tol=1e-9, abs_tol=1e-9)
            and math.isclose(self.imag, other.imag, rel_tol=1e-9, abs_tol=1e-9)
        )

    def __repr__(self) -> str:
        """
        Representação em string de um número complexo.

        Returns:
            str: representação no formato 'Complex(a, b)'.
        """
        return f"Complex({self.real}, {self.imag})"