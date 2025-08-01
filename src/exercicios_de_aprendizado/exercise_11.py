# Sum Square Difference - https://projecteuler.net/problem=6

def calculate_difference() -> int:
    sum_of_naturals = 0
    sum_of_squares = 0
    n = 1


    while n <= 100:
        sum_of_naturals += n
        sum_of_squares += n**2
        n += 1


    result = sum_of_naturals ** 2

    """
    Calcula a diferença entre:
    - o quadrado da soma dos 100 primeiros números naturais
    - e a soma dos quadrados desses mesmos números.

    Returns:
        int: A diferença entre o quadrado da soma e a soma dos quadrados.
    """
    return result - sum_of_squares

'''
Version interesting:

sum_of_squares = sum(n**2 for n in range(1, 101))


square_of_sum = sum(range(1, 101)) ** 2


print(square_of_sum - sum_of_squares)

'''