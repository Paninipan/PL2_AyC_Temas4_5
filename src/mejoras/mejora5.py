def seleccion_pedidos(pedidos, capacidad) -> list:
    """
    Ordenamos por benficio primeramente y luego por peso dentro de este orden.
        +Primero los que mas beneficio dan
        +Segundo de los que mas beneficio los que menos pesan
    Asignamos segun capacidad
    """
    pedidos_ordenados = sorted(pedidos, key=lambda x: (-x[2], x[1]))

    seleccionados = []
    capacidad_restante = capacidad

    # 2. Recorremos los pedidos y los añadimos si caben
    for pedido in pedidos_ordenados:
        peso_pedido = pedido[1]

        if peso_pedido <= capacidad_restante:
            seleccionados.append(pedido)
            capacidad_restante -= peso_pedido

        # Si la capacidad llega a 0, podemos terminar antes
        if capacidad_restante <= 0:
            break

    return seleccionados


# --- Prueba de empate ---
# Pedido 1 y 4 tienen el mismo beneficio (250), pero el 4 pesa menos.
pedido1 = [0, 400, 250, "A"]
pedido2 = [1, 24, 20, "B"]
pedido3 = [2, 50, 10, "C"]
pedido4 = [3, 300, 250, "D"] # Mismo beneficio que pedido1, menor peso.

pedidos = [pedido1, pedido2, pedido3, pedido4]

# Con capacidad 500, debería elegir el pedido 4 primero por pesar menos.
print(seleccion_pedidos(pedidos, 375))