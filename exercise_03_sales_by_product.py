# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("No existe el archivo")
    with open(filename, "r") as file:
        content = file.read()
        content = content.strip()
        conjuntos = content.split(";")
        diccionario = {}
        for par in conjuntos:
            if par != "":
                venta = par.split(":")
                producto = venta[0]
                monto = float(venta[1])
                if producto in diccionario:
                    diccionario[producto].append(monto)
                else:
                    diccionario[producto] = [monto]
        return diccionario


def process_sales(data):
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
