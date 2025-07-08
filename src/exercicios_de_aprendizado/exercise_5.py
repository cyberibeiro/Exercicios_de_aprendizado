n = 600851475143
x = 2
factors = []

while x <= n:
    if n % x == 0:
        factors.append(x)
        n = n // x
    else:
        x += 1

print(f'O maior fator primo do número', n, 'é:', factors[-1])