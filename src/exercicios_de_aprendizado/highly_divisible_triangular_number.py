# Project Euler - Highly Divisible Triangular Number:
# https://projecteuler.net/problem=12

from math import sqrt

def count_divisors(n: int) -> int:
    """
    Retorna a quantidade de divisores de 'n'.
    Usa o método da raiz quadrada: para cada divisor i encontrado,
    seu par n//i também é divisor, então contamos dois de uma vez.

    Args:
        n: O número inteiro a ser analisado.

    Returns:
        A quantidade de divisores de 'n'. Retorna 0 se n < 1.
    """
    if n < 1:
        return 0

    count = 0
    for divisor in range(1, int(sqrt(n)) + 1):
        if n % divisor == 0:
            count += 2

    if int(sqrt(n)) ** 2 == n:
        count -= 1

    return count


def first_triangular_with_more_than_n_divisors(min_divisors: int) -> int:
    """
    Retorna o primeiro número triangular que possui mais de 'min_divisors' divisores.
    Números triangulares são gerados pela soma acumulada dos naturais: 1, 3, 6, 10, 15...

    Args:
        min_divisors: O número mínimo de divisores (exclusivo).

    Returns:
        O primeiro número triangular com mais de 'min_divisors' divisores.
        Retorna -1 se não encontrado.
    """
    triangular = 0

    for triangle_index in range(1, int(1e9)):
        triangular += triangle_index
        if count_divisors(triangular) > min_divisors:
            return triangular

    return -1
