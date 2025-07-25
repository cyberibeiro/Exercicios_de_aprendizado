from math import gcd


def lcm(a, b) -> None:
    return abs(a * b) // gcd(a, b)


def smallest_multiple(n) -> int:
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result
