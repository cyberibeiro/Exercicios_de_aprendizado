naturais = []
n_elevado = []

n = 0

while n < 10:
    n += 1
    naturais.append(n)
    n_elevado.append(n**2) #salva o n já elevado a dois na lista

soma_naturais = sum(naturais)
resultado = soma_naturais ** 2

soma_elevados= sum(n_elevado)

print(f'A diferença entre o queadrado da soma e a soma dos quadrados dos primeiros números naturais é', resultado - soma_elevados)