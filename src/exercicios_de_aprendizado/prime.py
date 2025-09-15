def is_prime(number: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
        n (int): Número a ser testado.

    Returns:
        bool: True se for primo, False caso contrário.
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if not number % 2:
        return False

    index = 3

    while index * index <= number:
        if not number % index:
            return False
        index += 2

    return True


def nth_prime(nth: int) -> int:
    """
    Encontra o n-ésimo número primo.

    Args:
        n (int): Posição do primo desejado (ex: n=1 retorna 2, o primeiro primo).

    Returns:
        int: O n-ésimo número primo.
    """
    if nth < 1:
        raise ValueError("n deve ser >= 1")

    count, number = 0, 1

    while count < nth:
        number += 1
        if is_prime(number):
            count += 1

    return number
