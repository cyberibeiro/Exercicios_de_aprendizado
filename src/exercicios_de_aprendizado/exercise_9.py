from math import gcd


def lcm(a: int, b: int) -> int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return abs(a * b) // gcd(a, b)


def smallest_multiple(n: int) -> int:
    """Realiza o calculo do menor multiplo no intervalo determinado pelo limitante n

    Args:
        n (int): limite superior

    Returns:
        int: menor multiplo
    """
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result
