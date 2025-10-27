# Exercism - Prime Factors: https://exercism.org/tracks/python/exercises/prime-factors

def prime_factorization(to_factor: int) -> list[int]:
    """
    Calcula a fatoração prima de um número natural de forma otimizada.

    O algoritmo utiliza o método de Divisão por Tentativa otimizado (6k ± 1),
    que reduz significativamente o número de divisões necessárias em relação à
    versão tradicional. É eficiente para valores grandes de to_factor.

    Args:
        to_factor (int): O número inteiro positivo a ser fatorado.

    Returns:
        list[int]: Lista contendo os fatores primos de to_factor em ordem crescente.
                   Retorna uma lista vazia se to_factor <= 1.

    Raises:
        ValueError: Se to_factor não for um inteiro positivo.
    """
    if not isinstance(to_factor, int) or to_factor < 1:
        raise ValueError("A entrada deve ser um inteiro positivo.")

    if to_factor == 1:
        return []

    factors: list[int] = []

    while to_factor % 2 == 0:
        factors.append(2)
        to_factor //= 2

    while to_factor % 3 == 0:
        factors.append(3)
        to_factor //= 3

    factor = 5

    while factor * factor <= to_factor:
        while to_factor % factor == 0:
            factors.append(factor)
            to_factor //= factor

        while to_factor % (factor + 2) == 0:
            factors.append(factor + 2)
            to_factor //= factor + 2

        factor += 6

    if to_factor > 1:
        factors.append(to_factor)

    return factors
