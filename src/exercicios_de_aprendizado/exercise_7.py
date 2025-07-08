def find_the_largest_palindrome(beginning, end):
    largest_palindrome = 0
    for n1 in range(beginning, end + 1):
        for n2 in range(beginning, end + 1):
            product = n1 * n2
            str_product = str(product)
            if str_product == str_product[::-1]:
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome

result = find_the_largest_palindrome(100, 999)
print(f"O maior palíndromo é: {result}")