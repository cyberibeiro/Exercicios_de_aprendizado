class RotationalCipher:
    def __init__(self, text: str, key: int) -> None:
        """
        Inicializa a cifra com o texto e a chave de deslocamento.

        Args:
            text (str): O texto que será cifrado ou decifrado.
            key (int): O número de posições para o deslocamento da cifra.
        """
        self.text = text
        self.key = key

    def encrypt(self) -> str:
        """
        Aplica a cifra de César para encriptar o texto.

        Returns:
            str: O texto cifrado.
        """
        return self._shift(self.key)

    def decrypt(self) -> str:
        """
        Aplica a cifra de César para descriptografar o texto.

        Returns:
            str: O texto original decifrado.
        """
        return self._shift(-self.key)

    def _shift(self, shift: int) -> str:
        """
        Realiza o deslocamento dos caracteres no texto com base na chave.

        Args:
            shift (int): Quantidade de posições para deslocar (positiva ou negativa).

        Returns:
            str: O texto resultante após o deslocamento.
        """
        result = ""
        for char in self.text:
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += char
        return result