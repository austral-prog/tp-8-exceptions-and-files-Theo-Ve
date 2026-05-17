# Ejercicio 1 - Leer líneas de un archivo

def read_lines(filename):
        with open(filename, "r") as archivo:
            lista = []
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    lista.append(linea)
            return lista