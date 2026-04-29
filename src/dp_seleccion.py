"""
Este módulo contiene la función de seleccion de pedidos segun:
    -Cada pedido se representa como una estructura:
        + Pedido = (id, peso, beneficio, destino)
    -Entradas:
        + Una matriz de pedidos disponibles.
        + Una capacidad máxima de carga C.
    -Se debe seleccionar el subconjunto de pedidos que:
        + No exceda C.
        + Maximice el beneficio total.
        + Salida:
            -Lista de pedidos asignados:
                + Valor: Tupla 3 valors
                    * Id_Pedido
                    * Destino
                    * Beneficio

Solucion realizada medienate Programación Dinámica, descente recursivo.
    + Ordenar por beneficio
    + Asignar si peso < capacidad
    + Return si capacidad == 0 o matriz vacia.
"""
def seleccion_pedidos(pedidos, capacidad) -> list:
    cache = {}

    def seleccion_pedidos_dinamico(id_dic, capcidad):
        # Caso Base: No quedan pedidos o no hay capacidad
        if id_dic == len(pedidos) or capcidad <= 0:
            return 0, []

        # Comprobamos que la tupla este ya analizada
        existe = (id_dic, capcidad)
        if existe in cache:
            return cache[existe]

        # Si no lo incluimos sea como sea
        beneficio_sin, lista_sin = seleccion_pedidos_dinamico(id_dic + 1, capcidad)

        # Incluir el pedido actual si es posible
        peso_actual = pedidos[id_dic][1]
        beneficio_actual = pedidos[id_dic][2]

        if peso_actual <= capcidad:
            beneficio_con, lista_con = seleccion_pedidos_dinamico(id_dic + 1, capcidad-peso_actual)
            beneficio_con += beneficio_actual
            # Comparamos cuál de las dos opciones es mejor
            if beneficio_con > beneficio_sin:
                res = (beneficio_con, [pedidos[id_dic]] + lista_con)
            else:
                res = (beneficio_sin, lista_sin)
        else:
            res = (beneficio_sin, lista_sin)

        # 5. Guardar en cache la solución y retornar
        cache[existe] = res
        return res

    total_beneficio, seleccionados = seleccion_pedidos_dinamico(0, capacidad)
    return seleccionados

"""
Analisis complejidad
como la cache almacena 1 solucion para cada elemento. como mucho hay n soluciones
por lo que la complejidad -< O(n)
"""

def imprimir_camion(pedidos):
    print("Camion :")

    for pedido in pedidos:
        id_pedido, peso, beneficio, destino = pedido

        print(f"\t+ Pedido : {id_pedido}")
        print(f"\t\t+ Beneficio : {beneficio}")
        print(f"\t\t+ Peso : {peso}")
        print(f"\t\t+ Destino : {destino}")


# --- Prueba de empate ---

pedido1 = [0, 400, 250, "A"]
pedido2 = [1, 24, 20, "B"]
pedido3 = [2, 50, 10, "C"]
pedido4 = [3, 300, 250, "D"] # Mismo beneficio que pedido1, menor peso.

pedidos = [pedido1, pedido2, pedido3, pedido4]

seleccion = seleccion_pedidos(pedidos, 375)
imprimir_camion(seleccion)
