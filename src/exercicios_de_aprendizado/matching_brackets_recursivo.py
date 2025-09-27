class BracketMatcher:
    def __init__(
        self,
        text: str,
    ) -> None:
        """
        Inicializa com a string a ser verificada.

        Args:
            texto (str): Texto que pode conter (), [] e {}.
        """
        self.text = text

    def is_paired(self,) -> bool:
        """
        Verifica se a string está balanceada.

        Returns:
            bool: True se balanceado, False caso contrário.
        """
        pairs = {")": "(", "]": "[", "}": "{"}
        return self._check(
            self.text,
            [],
            pairs,
        )

    def _check(
        self,
        remaining: str,
        stack: list[str],
        pairs: dict[str, str],
    ) -> bool:
        """
        Função recursiva que processa a string caractere por caractere.

        Args:
            restante (str): Parte da string ainda não processada
            stack (list): Pilha de aberturas encontradas
            pairs (dict): Mapeamento de fechamento → abertura

        Returns:
            bool: True se balanceado, False caso contrário
        """
        if not remaining:
            return not stack

        char, rest = remaining[0], remaining[1:]
        opening = pairs.values()
        closing = pairs.keys()

        if char in opening:
            stack.append(char)

        elif char in closing and (not stack or stack.pop() != pairs[char]):
            return False

        return self._check(rest, stack, pairs)