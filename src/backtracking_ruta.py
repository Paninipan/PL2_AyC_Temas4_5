"""
Este módulo contiene la función de backtracking para encontrar la ruta óptima según:

    Una vez seleccionados los pedidos: 
        + Cada pedido tiene un punto de entrega. 
        + La ciudad se modela como una lista de tripletas:
            + Origen: Nombre del nodo
            + Destino: Nombre del nodo
            + Distancia: Distancia entre Or->Ds

    Se debe encontrar el orden de entrega que minimice la distancia total.
    
    Restricciones adicionales: 
        + Ventanas de tiempo máximas por pedido (opcional pero valorable). 
    
    Se deben implementar estrategias de poda:
        + por distancia acumulada
        + tiempo excedido, etc.). 

    Requisito obligatorio: 
        + El algoritmo debe usar backtracking explícito, no heurísticas voraces.


"""



def optimizar_ruta_backtracking(pedidos_asignados, matriz_distancias, ventanas_tiempo=None):

    # 1. Extraer destinos únicos de los pedidos asignados
    # Un mismo nodo puede tener varios pedidos, solo necesitamos visitarlo una vez.
    destinos_a_visitar = list(set([pedido[1] for pedido in pedidos_asignados]))

    # Variables globales para rastrear el estado óptimo
    mejor_ruta = []
    min_distancia = float('inf')
    distancia_max = 55

    def backtrack(nodo_actual, visitados, ruta_actual, distancia_actual, tiempo_actual):
        nonlocal mejor_ruta, min_distancia, distancia_max

        # PODA 1: Por distancia acumulada
        # Si la distancia de esta rama ya es mayor o igual a la mejor ruta encontrada, podamos.
        if distancia_actual >= min_distancia:
            return

        # PODA 2: Por ventanas de tiempo (Opcional)
        if ventanas_tiempo and nodo_actual in ventanas_tiempo:
            t_min, t_max = ventanas_tiempo[nodo_actual]
            # Si llegamos después de la ventana máxima de tiempo, podamos la rama
            if tiempo_actual > t_max:
                return
            # Si llegamos antes, esperamos (el tiempo avanza hasta t_min)
            tiempo_actual = max(tiempo_actual, t_min)
        if distancia_actual >= distancia_max:
            return
        # CASO BASE: Hemos visitado todos los destinos requeridos
        if len(visitados) == len(destinos_a_visitar):
            distancia_total = distancia_actual

            # Actualizamos la mejor solución encontrada
            if distancia_total < min_distancia:
                min_distancia = distancia_total
                mejor_ruta = ruta_actual.copy()
            return

        # RAMIFICACIÓN Y EXPLORACIÓN
        for destino in destinos_a_visitar:
            if destino not in visitados:
                distancia_viaje = matriz_distancias[nodo_actual][destino]
                # Si existe camino disponible al nodo destino calculamos
                if distancia_viaje >= 0:
                    # Para simplificar, asumimos que 1 unidad de distancia = 1 unidad de tiempo.
                    # En un entorno real, tendrías una matriz_tiempos independiente.
                    tiempo_viaje = distancia_viaje

                    # Modificamos el estado (Avanzar)
                    visitados.add(destino)
                    ruta_actual.append(destino)

                    # Llamada recursiva
                    backtrack(
                        destino,
                        visitados,
                        ruta_actual,
                        distancia_actual + distancia_viaje,
                        tiempo_actual + tiempo_viaje
                    )

                    # Restauramos el estado (Backtrack)
                    ruta_actual.pop()
                    visitados.remove(destino)

    # Inicialización del algoritmo
    # El nodo origen ya está en la ruta, pero no en 'visitados' (pues visitados controla los destinos)
    backtrack(nodo_actual=0,
              visitados=set(),
              ruta_actual=[0],
              distancia_actual=0,
              tiempo_actual=0)

    return mejor_ruta, min_distancia


def imprimir_nodos(lista_nodos):
    """
    [A]--dis-->[B]--dis-->[C]--/
    /--dis-->[D]--dis-->[E]--/
    /--dis-->[F]...
    :param lista_nodos:
    :return:
    """
    for nodo in lista_nodos:
        print(nodo)

# 1. Lista de pedidos asignados (Tupla: Id_Pedido, Destino, Beneficio)
pedidos_asignados = [
    ("P001", 1, 50),
    ("P002", 3, 80),
    ("P003", 1, 30),
    ("P004", 4, 120)
]

# 2. Matriz de distancias (Grafo ponderado de 5x5)
matriz_distancias = [
    [ 0, 10, 15, 20, 25],
    [10,  0, 35, 25, 30],
    [15, 35,  0, 30, 20],
    [20, 25, 30,  0, 15],
    [25, 30, 20, 15,  0]
]

# 3. Ventanas de tiempo opcionales {nodo: (t_min, t_max)}
# Si llegamos al nodo 3 después del tiempo 40, la poda descartará esa ruta.
ventanas_tiempo_ejemplo = {
    1: (0, 50),
    3: (0, 40),
    4: (0, 100)
}

# Ejecución del algoritmo
mejor_ruta, distancia_minima = optimizar_ruta_backtracking(
    pedidos_asignados=pedidos_asignados,
    matriz_distancias=matriz_distancias,
    ventanas_tiempo=ventanas_tiempo_ejemplo
)

print(f"Ruta óptima encontrada: {mejor_ruta}")
print(f"Distancia total: {distancia_minima}")


