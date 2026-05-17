# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("No existe el archivo")
    longest_word = ""
    with open(filename, 'r',) as file:
        text = file.read()
        words = text.split()

        if not words:
            raise ValueError("file has no words")

        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

    return longest_word
