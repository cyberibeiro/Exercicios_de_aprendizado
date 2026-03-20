# Exercism - Series:
# https://exercism.org/tracks/python/exercises/series


def slice(series: str, length: int) -> list[str]:
    """
    Retorna todas as substrings contíguas de tamanho 'length' da string 'series'.

    Percorre a string com uma janela deslizante de tamanho 'length', coletando
    cada substring na ordem em que aparece.

    Args:
        series: A string de dígitos a ser fatiada.
        length: O tamanho de cada substring (janela deslizante).

    Returns:
        Lista de substrings contíguas de tamanho 'length', na ordem de aparição.

    Raises:
        ValueError: Se 'series' for vazia, 'length' for zero, negativo,
                    ou maior que o comprimento de 'series'.
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[start : start + length] for start in range(len(series) - length + 1)]

    # resultado = []
    # for start in range(len(series) - length + 1):
    #     fatiamento = series[start : start + length]
    #     resultado.append(fatiamento)
    # return resultado
