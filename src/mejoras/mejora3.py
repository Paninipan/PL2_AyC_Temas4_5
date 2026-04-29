def seleccion_pedidos(pedidos, capacidad) -> list:
    """
    Algoritmo voraz, que añade los elemetos en el orden que llegan
    Si este elemento se puede añadir por capadidad, se añade.
    Sino se puede añadir se pasa al siguiente.
    """

    seleccionados = []
    capacidad_restante = capacidad

    # 2. Recorremos los pedidos y los añadimos si caben
    for elem in pedidos:
        peso_pedido = elem[1]

        if peso_pedido <= capacidad_restante:
            seleccionados.append(elem)
            capacidad_restante -= peso_pedido

        # Si la capacidad llega a 0, podemos terminar antes
        if capacidad_restante <= 0:
            break

    return seleccionados


# --- Prueba de empate ---
# Pedido 1 y 4 tienen el mismo beneficio (250), pero el 4 pesa menos.
pedido1 = [0, 2, 250, "A"]
pedido2 = [1, 24, 20, "B"]
pedido3 = [2, 50, 10, "C"]
pedido4 = [3, 300, 250, "D"] # Mismo beneficio que pedido1, menor peso.

pedidos = [pedido1, pedido2, pedido3, pedido4]

# Con capacidad 500, debería elegir el pedido 4 primero por pesar menos.
print(seleccion_pedidos(pedidos, 375))