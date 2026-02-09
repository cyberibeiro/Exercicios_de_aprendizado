import re


def generate_acronym(phrase: str) -> str:
    """
    Gera um acrônimo a partir de uma frase.

    O acrônimo é formado pela primeira letra de cada palavra da frase,
    convertida para maiúscula.

    Regras consideradas:
    - Espaços e hífens separam palavras.
    - Apóstrofos internos não separam palavras (ex: "It's" → "I").
    - Pontuação é ignorada.
    - Letras maiúsculas e minúsculas são tratadas igualmente.

    Exemplos:
        >>> generate_acronym("As Soon As Possible")
        "ASAP"
        >>> generate_acronym("Liquid-crystal display")
        "LCD"
        >>> generate_acronym("Thank George It's Friday!")
        "TGIF"
        >>> generate_acronym("First In, First Out")
        "FIFO"

    Args:
        phrase (str): frase de entrada para geração do acrônimo

    Returns:
        str: acrônimo gerado em letras maiúsculas
    """

# re é uma biblioteca de regras (padrões)
# no caso "Ache todas as sequências de letras que podem conter um apóstrofo (') no meio.”

    words: list[str] = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", phrase)
    acronym: str = "".join(word[0].upper() for word in words)

    return acronym