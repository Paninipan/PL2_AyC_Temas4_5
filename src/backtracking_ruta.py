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
    punto_inicio = "A"

    # ✔ Ventanas por ARISTA (CORRECTO)
    ventanas_aristas = {
        key: (n["tmin"], n["tmax"])
        for n in lista_nodos
        for key in [(n["origen"], n["destino"]), (n["destino"], n["origen"])]
    }

    # ✔ Distancias bidireccionales
    distancias = {}
    for n in lista_nodos:
        u, v, d = n["origen"], n["destino"], n["distancia"]
        distancias[(u, v)] = d
        distancias[(v, u)] = d

    destinos_a_visitar = list(set([p[3] for p in pedidos_asignados]))

    if punto_inicio in destinos_a_visitar:
        destinos_a_visitar.remove(punto_inicio)

    mejor_ruta = []
    min_distancia = float('inf')

    def backtrack(nodo_actual, visitados, ruta_actual, distancia_actual, tiempo_actual):

        nonlocal mejor_ruta, min_distancia

        # podamos por la distancia, si la distancia actual supera a la minima encontrada
        if distancia_actual >= min_distancia:
            return

        # Caso base del backtracking, hay 1 nodo y es el que hay que visitar
        if len(visitados) == len(destinos_a_visitar):
            #Copiamos la ruta del caso base y devolvemos
            mejor_ruta = ruta_actual.copy()
            min_distancia = distancia_actual
            return

        # RAMIFICACIÓN del "arbol" de posibilidades
        for destino in destinos_a_visitar:

            #Si el destino ya ha sido visitado pasamos
            if destino in visitados:
                continue
            #Si la arista del grafo no existe pasamos
            if (nodo_actual, destino) not in distancias:
                continue

            # Accedemos a la distancia de la arista actual-destino y sumamos la ruta
            distancia_viaje = distancias[(nodo_actual, destino)]
            nuevo_tiempo = tiempo_actual + distancia_viaje

            # La arista es como la carretera entre los nodos y donde el primer acceso y la última salida lo limitan los tmin y tmax
            arista = (nodo_actual, destino)

            #Si la arista tiene restricciones de tiempo miramos si estamos en el valor adecuado
            if arista in ventanas_aristas:
                t_min, t_max = ventanas_aristas[arista]

                #Si el valor del llegada al nodo destino es superior
                if nuevo_tiempo > t_max:
                    continue  # demasiado tarde → poda

                #Si el valor de llegada al destino es inferior
                if nuevo_tiempo < t_min:
                    nuevo_tiempo = t_min  # espera

            #Añadimos el nodo a visitados y a la ruta
            visitados.add(destino)
            ruta_actual.append(destino)

            #Hacemos la llamada del backtracking
            backtrack(
                destino,
                visitados,
                ruta_actual,
                distancia_actual + distancia_viaje,
                nuevo_tiempo
            )
            #Sacamos la ruta y el nodo
            ruta_actual.pop()
            visitados.remove(destino)

    #llamada inicial del backtracking
    backtrack(
        punto_inicio,
        set(),
        [punto_inicio],
        0,
        0
    )

    # Construcción de ruta final de manera detallada para la impresión
    ruta_detallada = []

    #Recorremos todos los nodos de la ruta
    for i in range(len(mejor_ruta) - 1):
        o, d = mejor_ruta[i], mejor_ruta[i + 1]
        ruta_detallada.append((o, d, distancias.get((o, d))))

    return ruta_detallada, min_distancia

#Funcion para imprimir los nodos de la ruta minima
def imprimir_nodos(lista_nodos):
    """
    Sigue más o menos la siguiente estructura
    [A]--dis-->[B]--dis-->[C]--/
     /--dis-->[D]--dis-->[E]--/
     /--dis-->[F]...
     """
    for nodo in lista_nodos:
        origen = nodo[0]
        destino = nodo[1]
        distancia = nodo[2]
        print(f"[{origen}] --{distancia}--> [{destino}]")
