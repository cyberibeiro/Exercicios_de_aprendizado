# Diferença da Soma Quadrada - https://projecteuler.net/problem=6

def calculate_difference():

sum_of_squares = 0
n = 0
sum_total = 0

while n <= 100:
    sum_of_squares += number**2
    number += 1

for x in range(101):
    sum_total += x
    square_of_sum = sum_total ** 2

return square_of_sum - sum_of_squares

'''
Version interesting:

sum_of_squares = sum(n**2 for n in range(1, 101))


square_of_sum = sum(range(1, 101)) ** 2


print(square_of_sum - sum_of_squares)

'''