# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    with open(filename, 'r') as archivo:
        lineas = archivo.read().split("\n")
        header = lineas[0].split(",")
        lista = []
        for linea in lineas[1:]:
            if linea.strip() != "":
                valores = linea.split(",")
                diccionario = {
                    'name': valores[0],
                    'age': int(valores[1]),
                    'city': valores[2]
                }
                lista.append(diccionario)
        return lista
