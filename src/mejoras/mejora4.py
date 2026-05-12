import json
import heapq


def prim_busqueda(nodos_mapa):

    # Usamos un diccionario donde cada llave es un nodo y el valor es una lista de (distancia, destino)
    grafo = {}
    nodos_unicos = set()

    for nodo in nodos_mapa:
        origen, destino, distancia = nodo['origen'], nodo['destino'], nodo['distancia']

        nodos_unicos.add(origen)
        nodos_unicos.add(destino)

        if origen not in grafo: grafo[origen] = []
        if destino not in grafo: grafo[destino] = []

        grafo[origen].append((distancia, destino))
        grafo[destino].append((distancia, origen))

    # 2. Inicializar Prim
    nodo_inicio = list(nodos_unicos)[0]  #Empezamos por el primer nodo
    ruta = []
    visitados = {nodo_inicio}

    # Cola de prioridad: (distancia, origen, destino)
    vecinos = [(dist, nodo_inicio, dest) for dist, dest in grafo[nodo_inicio]]
    heapq.heapify(vecinos)

    costo_total = 0

    # 3. Bucle principal para el algoritmo de Prim
    while vecinos:
        distancia, origen, destino = heapq.heappop(vecinos)

        if destino not in visitados:
            visitados.add(destino)
            ruta.append({'desde': origen, 'hacia': destino, 'distancia': distancia})
            costo_total += distancia

            for proxima_distancia, vecino in grafo[destino]:
                if vecino not in visitados:
                    heapq.heappush(vecinos, (proxima_distancia, destino, vecino))

    return ruta, costo_total

