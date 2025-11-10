# Project Euler (Special Pythagorean Triplet)
# https://projecteuler.net/problem=9


def find_pythagorean_triplet(total_sum: int = 1000) -> tuple[
    int,
    int,
    int,
    int,
]:
    """
    Encontra a tripla pitagórica (a, b, c) tal que:
    - a^2 + b^2 = c^2
    - a + b + c = total_sum (por padrão 1000)
    Retorna uma tupla (a, b, c, produto)
    """
    result = (0, 0, 0, 0)

    for a in range(1, total_sum):  # evita repetição e dar negativo
        for b in range(a + 1, total_sum):
            c = total_sum - a - b

            if a**2 + b**2 == c**2:
                result = (a, b, c, a * b * c)
                break

        if any(result):
            break

    return result
