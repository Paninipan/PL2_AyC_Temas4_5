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
def optimizar_ruta_backtracking(pedidos_asignados, lista_nodos):
    """
    Versión adaptada para trabajar con la estructura de datos de los generadores:
    - lista_nodos: [{"origen": "A", "destino": "B", "distancia": 10}, ...]
    - pedidos_asignados: [(id, peso, beneficio, destino), ...]
    """
    punto_inicio = "A"
    ventanas_tiempo = None

    # 1. Transformar lista de nodos en un mapa de distancias para búsqueda O(1)
    # Como los generadores suelen dar rutas en un sentido, asumimos bidireccionalidad
    distancias = {}
    nodos_existentes = set()
    for n in lista_nodos:
        u, v, d = n["origen"], n["destino"], n["distancia"]
        distancias[(u, v)] = d
        distancias[(v, u)] = d  # Simetría para poder volver o movernos libremente
        nodos_existentes.add(u)
        nodos_existentes.add(v)

    # 2. Extraer destinos únicos de los pedidos (el destino es el índice 3 según Source 2)
    destinos_a_visitar = list(set([pedido[3] for pedido in pedidos_asignados]))

    # Si el punto de inicio está en los destinos, lo quitamos de la lista "a visitar"
    # para no procesarlo doble, pero debe estar en la ruta inicial.
    if punto_inicio in destinos_a_visitar:
        destinos_a_visitar.remove(punto_inicio)

    mejor_ruta = []
    min_distancia = float('inf')
    distancia_max_limite = 500  # Ajustado según los rangos del generador

    def backtrack(nodo_actual, visitados, ruta_actual, distancia_actual, tiempo_actual):
        nonlocal mejor_ruta, min_distancia

        # PODA 1: Por distancia acumulada
        if distancia_actual >= min_distancia:
            return

        # PODA 2: Ventanas de tiempo
        if ventanas_tiempo and nodo_actual in ventanas_tiempo:
            t_min, t_max = ventanas_tiempo[nodo_actual]
            if tiempo_actual > t_max:
                return
            tiempo_actual = max(tiempo_actual, t_min)

        # CASO BASE: Todos los destinos visitados
        if len(visitados) == len(destinos_a_visitar):
            if distancia_actual < min_distancia:
                min_distancia = distancia_actual
                mejor_ruta = ruta_actual.copy()
            return

        # RAMIFICACIÓN
        for destino in destinos_a_visitar:
            if destino not in visitados:
                # Verificar si existe conexión en el mapa de distancias
                if (nodo_actual, destino) in distancias:
                    distancia_viaje = distancias[(nodo_actual, destino)]

                    # Aplicar movimiento
                    visitados.add(destino)
                    ruta_actual.append(destino)

                    backtrack(
                        destino,
                        visitados,
                        ruta_actual,
                        distancia_actual + distancia_viaje,
                        tiempo_actual + distancia_viaje  # 1 unidad dist = 1 unidad tiempo
                    )

                    # Backtrack
                    ruta_actual.pop()
                    visitados.remove(destino)

    # Inicialización
    backtrack(nodo_actual=punto_inicio,
              visitados=set(),
              ruta_actual=[punto_inicio],
              distancia_actual=0,
              tiempo_actual=0)
    # Construir lista de tramos (origen, destino, distancia)
    ruta_detallada = []

    for i in range(len(mejor_ruta) - 1):
        origen = mejor_ruta[i]
        destino = mejor_ruta[i + 1]

        if (origen, destino) in distancias:
            d = distancias[(origen, destino)]
        else:
            # si no existe conexión directa (por seguridad)
            d = None

        ruta_detallada.append((origen, destino, d))

    return ruta_detallada, min_distancia


def imprimir_nodos(lista_nodos):
    """
    [A]--dis-->[B]--dis-->[C]--/
    /--dis-->[D]--dis-->[E]--/
    /--dis-->[F]...
    """
    print(lista_nodos)
    # for nodo in lista_nodos:
      #  origen = nodo[1]
       # destino = nodo[2]
        #distancia = nodo[3]
        #print(f"[{origen}] --{distancia}--> [{destino}]")