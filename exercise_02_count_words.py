# Ejercicio 2 - Contar palabras en un archivo


def count_words(filename):
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("No existe el archivo")

    words_dict = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line = line.lower()
            words_list = line.split()
            for word in words_list:
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
        return words_dict