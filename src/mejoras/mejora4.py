import json
import heapq


def prim_mst(conexiones):
    # 1. Construir la lista de adyacencia
    # Usamos un diccionario donde cada llave es un nodo y el valor es una lista de (distancia, destino)
    grafo = {}
    nodos_unicos = set()

    for c in conexiones:
        u, v, d = c['origen'], c['destino'], c['distancia']
        nodos_unicos.add(u)
        nodos_unicos.add(v)
        if u not in grafo: grafo[u] = []
        if v not in grafo: grafo[v] = []
        grafo[u].append((d, v))
        grafo[v].append((d, u))

    # 2. Inicializar Prim
    start_node = list(nodos_unicos)[0]  # Empezamos por cualquier nodo (ej. 'A')
    ruta = []
    visitados = {start_node}
    # Cola de prioridad: (distancia, origen, destino)
    edges = [(d, start_node, v) for d, v in grafo[start_node]]
    heapq.heapify(edges)

    costo_total = 0

    # 3. Bucle principal
    while edges:
        distancia, u, v = heapq.heappop(edges)

        if v not in visitados:
            visitados.add(v)
            ruta.append({'desde': u, 'hacia': v, 'distancia': distancia})
            costo_total += distancia

            for proxima_distancia, vecino in grafo[v]:
                if vecino not in visitados:
                    heapq.heappush(edges, (proxima_distancia, v, vecino))

    return ruta, costo_total

