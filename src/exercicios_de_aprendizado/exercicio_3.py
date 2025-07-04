# f(n) = f(n-1) + f(n-2)
# f(1) = 1
# f(2) = 1
# f(3) = f(2) + f(1)
# f(3) = 1 + 1
# f(3) = 2
def fibonacci(n):
    return 1 if 1 == n or 2 == n else fibonacci(n-1) + fibonacci(n-2)

def exercicio_3_ruim(limit):
    pares = []
    n = 1
    fn = fibonacci(n)

    while fn <= limit:
        fn = fibonacci(n)
        n = n + 1
        if fn % 2 == 0:
            pares.append(fn)

    return sum(pares)

def exercicio_3(limit):
    novo_termo = []
    f = 1
    fn = 2

    while fn <= limit:
        if fn % 2 == 0:
            novo_termo.append(fn)
        f, fn = fn, f + fn

    return novo_termo

print("Soma dos pares:", exercicio_3_ruim(4_000_000))