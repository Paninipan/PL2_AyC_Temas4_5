"""
Este módulo contiene la función de seleccion de pedidos según:
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
                + Valor: Tupla 3 valores
                    * Id_Pedido
                    * Destino
                    * Beneficio

Solución realizada mediante Programación Dinámica, descente recursivo.
    + Ordenar por beneficio
    + Asignar si peso < capacidad
    + Return si capacidad == 0 o matriz vacia.
"""
def seleccion_pedidos(pedidos, capacidad) -> list:
    cache = {}

    def seleccion_pedidos_dinamico(id_dic, capacidad):

        # Caso Base: No quedan pedidos o no hay capacidad
        if id_dic == len(pedidos) or capacidad <= 0:
            return 0, []

        # Comprobamos si la tupla (pedido, capacidad) ya está analizada
        existe = (id_dic, capacidad)
        if existe in cache:
            return cache[existe]

        # Si no lo incluimos, pasamos de pedido
        beneficio_sin, lista_sin = seleccion_pedidos_dinamico(id_dic + 1, capacidad)

        # Para incluirlo, calculamos el peso y beneficio del pedido
        peso_actual = pedidos[id_dic][1]
        beneficio_actual = pedidos[id_dic][2]

        # Incluimos el pedido actual si es posible
        if peso_actual <= capacidad:
            beneficio_con, lista_con = seleccion_pedidos_dinamico(id_dic + 1, capacidad-peso_actual)
            beneficio_con += beneficio_actual

            # Comparamos cuál de las dos opciones es mejor
            if beneficio_con > beneficio_sin:
                res = (beneficio_con, [pedidos[id_dic]] + lista_con)
            else:
                res = (beneficio_sin, lista_sin)
        else:
            res = (beneficio_sin, lista_sin)

        # Guardamos en la cache el estado junto a la solución y retornamos 
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



