# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("No existe el archivo")
    with open(filename) as file:
        lista = []
        for line in file:
            try:
                line = float(line)
                lista.append(line)
            except ValueError:
                pass

        if len(lista) == 0:
            raise ValueError("no valid numbers")

        return sum(lista) / len(lista)