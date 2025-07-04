def exercicio_1(limit):
    multiplos = []
    n = 1

    while n < limit:
        if n % 3 == 0 or n % 5 == 0:
            multiplos.append(n)
        n += 1

    return multiplos

print("A soma de todos os múltiplos de 3 e 5 é ", sum(exercicio_1(10)))