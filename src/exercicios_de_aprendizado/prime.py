def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def nth_prime(n: int) -> int:
    if n < 1:
        raise ValueError("n deve ser >= 1")
    count, num = 0, 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num
