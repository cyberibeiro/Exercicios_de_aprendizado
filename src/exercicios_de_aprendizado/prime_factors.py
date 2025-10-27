# Exercism - Prime Factors: https://exercism.org/tracks/python/exercises/prime-factors


def prime_factorization(n: int) -> list[int]:
    """
    Calcula a fatoração prima de um número natural de forma otimizada.

    O algoritmo utiliza o método de Divisão por Tentativa otimizado (6k ± 1),
    que reduz significativamente o número de divisões necessárias em relação à
    versão tradicional. É eficiente para valores grandes de n.

    Args:
        n (int): O número inteiro positivo a ser fatorado.

    Returns:
        list[int]: Lista contendo os fatores primos de n em ordem não decrescente.
                   Retorna uma lista vazia se n <= 1.

    Raises:
        ValueError: Se n não for um inteiro positivo.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("A entrada deve ser um inteiro positivo.")

    if n == 1:
        return []

    factors: list[int] = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    while n % 3 == 0:
        factors.append(3)
        n //= 3

    i = 5
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i

        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= i + 2

        i += 6

    if n > 1:
        factors.append(n)

    return factors
