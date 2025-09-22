class BracketMatcher:
    def __init__(
        self,
        texto: str,
    ) -> None:
        """
        Inicializa com a string a ser verificada.

        Args:
            string (str): Texto de entrada que pode conter (), [] e {}.
        """
        self.string = texto

    def is_paired(self) -> bool:
        """
        Verifica se a string contém parênteses, colchetes e chaves
        corretamente balanceados e aninhados.

        Returns:
            bool: True se balanceado, False caso contrário.
        """
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        opening = pairs.keys()
        closing = pairs.values()
        stack: list[str] = []

        for character in self.string:
            if character in opening:
                stack.append(character)
            elif character in closing and (not stack or stack.pop() != pairs[character]):
                return False

        return not stack
