# f(n) = f(n-1) + f(n-2)
# f(1) = 1
# f(2) = 1
# f(3) = f(2) + f(1)
# f(3) = 1 + 1
# f(3) = 2
def fibonacci(n: int) -> int:
    return 1 if 1 == n or 2 == n else fibonacci(n - 1) + fibonacci(n - 2)


def exercise_3_bad(limit: int) -> int:
    pairs: list[int] = []
    n = 1
    fn = fibonacci(n)

    while fn <= limit:
        fn = fibonacci(n)
        n = n + 1
        if fn % 2 == 0:
            pairs.append(fn)

    return sum(pairs)


def exercise_3(limit: int) -> int:
    new_term: list[int] = []
    f = 1
    fn = 2

    while fn <= limit:
        if fn % 2 == 0:
            new_term.append(fn)
        f, fn = fn, f + fn

    return sum(new_term)


print("Soma dos pares:", exercise_3(4_000_000))
