def exercise_4() -> int:

    natural: list[int] = []
    n_raised: list[int] = []

    n = 0

    while n < 10:
        n += 1
        natural.append(n)
        n_raised.append(n**2)

    add_natural = sum(natural)
    result = add_natural ** 2

    add_raised = sum(n_raised)

    return result - add_raised