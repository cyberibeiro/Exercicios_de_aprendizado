def encontrar_maior_palindromo(inicio, fim):
    maior_palindromo = 0
    for n1 in range(inicio, fim + 1):
        for n2 in range(inicio, fim + 1):
            produto = n1 * n2
            str_produto = str(produto)
            if str_produto == str_produto[::-1]:
                if produto > maior_palindromo:
                    maior_palindromo = produto
    return maior_palindromo


resultado = encontrar_maior_palindromo(100, 999)
print(f"O maior palíndromo produto de dois números de 3 dígitos é: {resultado}")