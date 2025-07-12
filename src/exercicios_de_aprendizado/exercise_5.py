def biggest_prime_factor(n: int) -> int:
    x = 2
    factors = []

    while x <= n:
        if n % x == 0:
            factors.append(x)
            n = n // x
        else:
            x += 1

    return factors[-1]
