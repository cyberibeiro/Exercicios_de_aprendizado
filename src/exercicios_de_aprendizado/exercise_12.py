def pig_latin(word: str) -> str:
    """
    Converte uma palavra para Pig Latin.

    Regras:
    - Se começar com vogal ou com 'xr' ou 'yt', adiciona 'ay' ao final.
    - Se contiver 'qu', move 'qu' e o que vem antes para o final e adiciona 'ay'.
    - Caso contrário, move o grupo de consoantes iniciais até a primeira vogal (ou 'y')
      para o final e adiciona 'ay'.

    Args:
        word (str): A palavra a ser convertida.

    Returns:
        str: A palavra convertida para Pig Latin.
    """

    VOGAIS = ['a', 'e', 'i', 'o', 'u']

    if word.startswith('xr') or word.startswith('yt') or word[0] in VOGAIS:
        return word + 'ay'

    elif "qu" in word:
        qu_index = word.find("qu")
        rest_of_word = word[qu_index + 2:]
        consonant_cluster = word[:qu_index + 2]
        return rest_of_word + consonant_cluster + "ay"

    else:
        VOGAIS_E_Y = VOGAIS + ['y']
        first_vowel_index = 0

        for letter in word:
            if letter in VOGAIS_E_Y:
                break
            first_vowel_index += 1

        consonants = word[:first_vowel_index]
        rest_of_word = word[first_vowel_index:]

        return rest_of_word + consonants + 'ay'


def translate(sentence: str) -> str:
    """
    Converte uma frase para Pig Latin, palavra por palavra.

    Args:
        sentence (str): Frase composta por uma ou mais palavras.

    Returns:
        str: Frase traduzida para Pig Latin.
    """
    words = sentence.split()
    translated = [pig_latin(word) for word in words]
    return ' '.join(translated)