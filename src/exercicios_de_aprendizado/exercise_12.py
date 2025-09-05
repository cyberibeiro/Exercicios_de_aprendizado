class PigLatin:
    """
    Classe para converter palavras e frases para Pig Latin.

    Regras:
    - Se a palavra começar com vogal, ou com 'xr' ou 'yt', adiciona 'ay' ao final.
    - Se contiver 'qu', move 'qu' e o que vem antes para o final e adiciona 'ay'.
    - Caso contrário, move o grupo de consoantes iniciais até a primeira vogal (ou 'y')
      para o final e adiciona 'ay'.
    """

    def __init__(self):
        self.VOGAIS = ['a', 'e', 'i', 'o', 'u']

    def _translate_word(self, word: str) -> str:
        """
        Traduz uma única palavra para Pig Latin.
        """
        if word.startswith('xr') or word.startswith('yt') or word[0] in self.VOGAIS:
            return word + 'ay'

        elif "qu" in word:
            qu_index = word.find("qu")
            rest_of_word = word[qu_index + 2:]
            consonant_cluster = word[:qu_index + 2]
            return rest_of_word + consonant_cluster + "ay"

        else:
            VOGAIS_E_Y = self.VOGAIS + ['y']
            first_vowel_index = 0

            for letter in word:
                if letter in VOGAIS_E_Y:
                    break
                first_vowel_index += 1

            consonants = word[:first_vowel_index]
            rest_of_word = word[first_vowel_index:]

            return rest_of_word + consonants + 'ay'

    def translate(self, sentence: str) -> str:
        """
        Traduz uma frase inteira para Pig Latin.
        """
        words = sentence.split()
        translated = [self._translate_word(word) for word in words]
        return ' '.join(translated)
