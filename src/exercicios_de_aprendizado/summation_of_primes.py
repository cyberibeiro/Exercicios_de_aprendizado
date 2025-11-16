# Project Euler - Summation of Primes : https://projecteuler.net/problem=10

def sum_primes_below(limit: int) -> int:
    """
    Retorna a soma de todos os números primos menores que 'limit'.
    Implementa o algoritmo do Crivo de Eratóstenes.
    """
    if limit < 2:
        return 0

    sieve = [True] * limit
    sieve[0:2] = [False, False]

    prime = 2
    while prime * prime < limit:
        if sieve[prime]:
            for multiple in range(prime * prime, limit, prime):
                sieve[multiple] = False
        prime += 1

    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
