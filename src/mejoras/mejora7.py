def calcular_distancias_minimas(lista_nodos):
    """
    Toma la lista de nodos original y precalcula la distancia mínima entre 
    cualquier par de nodos de la ciudad, devolviendo un diccionario.
    """
    distancias = {}
    nodos = set()

    # 1. Inicializar el grafo con las conexiones directas
    for n in lista_nodos:   
        u, v, d = n["origen"], n["destino"], n["distancia"]
        nodos.add(u)
        nodos.add(v)
        distancias[(u, v)] = d
        distancias[(v, u)] = d 

    # 2. La distancia de un nodo a sí mismo es 0
    for nodo in nodos:
        distancias[(nodo, nodo)] = 0

    # 3. El núcleo de Floyd-Warshall
    # Para cada nodo intermedio (k), vemos si ir de i a j pasando por k es más corto
    for k in nodos:
        for i in nodos:
            for j in nodos:
                # Si existe un camino de i->k y de k->j
                if (i, k) in distancias and (k, j) in distancias:
                    nueva_distancia = distancias[(i, k)] + distancias[(k, j)]
                    
                    # Si no había camino previo de i->j, o el nuevo es mejor, lo actualizamos
                    if (i, j) not in distancias or nueva_distancia < distancias[(i, j)]:
                        distancias[(i, j)] = nueva_distancia
                        distancias[(j, i)] = nueva_distancia

    return distancias

# --- Prueba de Mejora 7: Floyd-Warshall ---

lista_nodos = [
    {"origen": "A", "destino": "B", "distancia": 10},
    {"origen": "B", "destino": "C", "distancia": 10},
    {"origen": "A", "destino": "C", "distancia": 100}
]

print("Calculando la matriz de distancias mínimas...")
distancias = calcular_distancias_minimas(lista_nodos)

print("\nDistancia mínima de A a B (Debería ser 10):")
print(distancias.get(("A", "B")))

print("\nDistancia mínima de B a C (Debería ser 10):")
print(distancias.get(("B", "C")))

print("\nDistancia mínima de A a C (Debería ser 20):")
print(distancias.get(("A", "C")))

print("\nDistancia de un nodo a sí mismo (A a A, debería ser 0):")
print(distancias.get(("A", "A")))