def caesar_cipher(text, key) -> None:
    result = ""


    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char


    return result