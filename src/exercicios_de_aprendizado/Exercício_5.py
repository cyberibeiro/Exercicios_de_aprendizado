n = 600851475143
x = 2
fatores = []

while x <= n:
    if n % x == 0:
        fatores.append(x)
        n = n // x  
    else:
        x += 1

print(f'O maior fator primo do número', n, 'é:', fatores[-1])    # -1 pega o ultimo elemento