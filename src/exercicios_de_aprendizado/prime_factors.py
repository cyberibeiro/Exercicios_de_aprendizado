#Exercism - Prime Factors: https://exercism.org/tracks/python/exercises/prime-factors

from typing import List

def prime_factors(number: int) -> list[int]:
    """
    Computa a fatoração prima de um número natural.

    Utiliza o método de Divisão por Tentativa otimizado (Trial Division)
    para encontrar todos os fatores primos, incluindo repetições.

    Args:
        number (int): O número natural a ser fatorado.

    Returns:
        list[int]: Uma lista de inteiros contendo os fatores primos do número,
                   em ordem não decrescente. Retorna uma lista vazia para números <= 1.
    """
    if number <= 1:
        return []

    factors: list[int] = []
    current_number: int = number
    divisor: int = 3

    while current_number % 2 == 0:
        factors.append(2)
        current_number //= 2

    while divisor * divisor <= current_number:
        if current_number % divisor == 0:
            factors.append(divisor)
            current_number //= divisor
        else:
            divisor += 2

    if current_number > 1:
        factors.append(current_number)

    return factors