# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("No existe el archivo")

    with open(filename, 'r') as archivo:
        resultado = {}
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                partes = linea.split(":")
                nombre = partes[0]
                notas = [float(nota) for nota in partes[1].split(",")]
                promedio = sum(notas) / len(notas)
                maximo = max(notas)
                minimo = min(notas)
                resultado[nombre] = (promedio, maximo, minimo)
        return resultado

