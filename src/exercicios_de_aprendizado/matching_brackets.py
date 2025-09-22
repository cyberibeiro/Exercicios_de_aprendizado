from typing import List
class BracketMatcher:
    def __init__(self, string: str) -> None:
        """
        Inicializa com a string a ser verificada.

        Args:
            string (str): Texto de entrada que pode conter (), [] e {}.
        """
        self.string = string

    def is_paired(self) -> bool:
        """
        Verifica se a string contém parênteses, colchetes e chaves
        corretamente balanceados e aninhados.

        Returns:
            bool: True se balanceado, False caso contrário.
        """
        pairs = {")": "(", "]": "[", "}": "{"}
        stack: List[str] = []

        for character in self.string:
            if character in "([{":
                stack.append(character)
            elif character in ")]}":
                if not stack or stack.pop() != pairs[character]:
                    return False

        return not stack
