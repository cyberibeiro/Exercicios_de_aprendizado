class PigLatin:
    """
    Classe para converter palavras e frases para Pig Latin.

    Regras:
    - Se a palavra começar com vogal, ou com 'xr' ou 'yt', adiciona 'ay' ao final.
    - Se contiver 'qu' em qualquer parte após consoantes iniciais, move esse grupo
      (até e incluindo 'qu') para o final e adiciona 'ay'.
    - Caso contrário, move o grupo de consoantes iniciais até a primeira vogal
      (ou 'y', exceto se for inicial) para o final e adiciona 'ay'.
    """

    def __init__(self) -> None:
        self.vowels = ["a", "e", "i", "o", "u"]

    
    def _translate_word(self, word: str) -> str:
        """
        Traduz uma única palavra para Pig Latin.
        """
        if word.startswith("xr") or word.startswith("yt") or word[0] in self.vowels:
            return word + "ay"


        qu_index = word.find("qu")
        if qu_index != -1:
            rest_of_word = word[qu_index + 2 :]
            consonant_cluster = word[: qu_index + 2]
            return rest_of_word + consonant_cluster + "ay"


        for i, letter in enumerate(word):
            if letter in self.vowels or (letter == "y" and i > 0):
                first_vowel_index = i
                break
        else:
            first_vowel_index = len(word)

        consonants = word[:first_vowel_index]
        rest_of_word = word[first_vowel_index:]
        return rest_of_word + consonants + "ay"

    def translate(self, sentence: str) -> str:
        """
        Traduz uma frase inteira para Pig Latin.
        """
        words = sentence.split()
        translated = [self._translate_word(word) for word in words]
        return " ".join(translated)

