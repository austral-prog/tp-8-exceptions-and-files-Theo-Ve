# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    items_ordenados = sorted(inventory.keys())
    with open(filename, 'w') as file:
        for item in items_ordenados:
            cantidad = inventory[item]
            file.write(f"{item}:{cantidad}\n")
