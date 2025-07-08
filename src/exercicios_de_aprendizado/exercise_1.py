def exercise_1(limit: int) -> int:
    multiplos: list[int] = []
    n = 1

    while n < limit:
        if n % 3 == 0 or n % 5 == 0:
            multiplos.append(n)
        n += 1

    return sum(multiplos)