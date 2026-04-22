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




#prueba
#Pedido = (id, peso, beneficio, destino)
pedido1 = [0, 50, 250, "A"]
pedido2 = [1, 25, 20, "A"]
pedido3 = [2, 45, 21, "A"]
pedido4 = [3, 1, 100, "A"]
pedido5 = [4, 1, 100, "A"]
pedido6 = [5, 1, 100, "A"]
pedido7 = [6, 1, 100, "A"]
pedido8 = [7, 1, 100, "A"]
pedido9 = [8, 20, 20, "A"]

pedidos = [pedido1, pedido2, pedido3, pedido4, pedido5, pedido6,pedido7, pedido8, pedido9]

print(seleccion_pedidos(pedidos,100))
