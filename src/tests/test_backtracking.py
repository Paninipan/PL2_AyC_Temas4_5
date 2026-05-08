from backtracking_ruta import optimizar_ruta_backtracking

def test_1_ruta_optima():
    """
    Verifica que en un grafo simple y pequeño, el algoritmo 
    encuentra el camino más corto visitando todos los nodos.
    """
    print("Ejecutando Test 1: [Ruta óptima]")
    
    nodos = [
        {"origen": "A", "destino": "B", "distancia": 10},
        {"origen": "B", "destino": "C", "distancia": 10},
        {"origen": "A", "destino": "C", "distancia": 50}    
    ]
    
    pedidos = [
        [1, 5, 10, "B"],
        [2, 5, 10, "C"]
    ]
    
    ruta_optima, min_distancia = optimizar_ruta_backtracking(pedidos, nodos)
    
    assert min_distancia == 20, f"Error: La distancia esperada era 20, pero fue {min_distancia}."
    
    # Comprobamos que la ruta es [A]-->[B]-->[C]
    nodos_ruta = [tramo[1] for tramo in ruta_optima]
    assert nodos_ruta == ["B", "C"], f"Error: La ruta óptima debe visitar B y luego C, pero fue {nodos_ruta}."
    print("Test 1: [Ruta óptima] superado con éxito.\n")

def test_2_ruta_optima():
    """
    Demuestra que el algoritmo explora todas las ramas y no cae en 
    la trampa de tomar el camino más corto inicial si eso le obliga
    a tomar caminos carísimos después.
    """
    print("Ejecutando Test 2: [Ruta óptima]")
    
    # Si utilizasemos un algoritmo voraz: [A]--1-->[B]. Desde B, para visitar C y D,
    # da igual cual elijamos, existe una distancia de 100. Distancia total = 111.
    # Ruta óptima: [A]--10-->[C]--10-->[B]--10-->[D]. Distancia total = 30.
    nodos = [
        {"origen": "A", "destino": "B", "distancia": 1},
        {"origen": "A", "destino": "C", "distancia": 10},
        {"origen": "B", "destino": "D", "distancia": 10},
        {"origen": "B", "destino": "C", "distancia": 10},
        {"origen": "C", "destino": "D", "distancia": 100} 
    ]
    pedidos = [
        [1, 1, 1, "B"],
        [2, 1, 1, "C"],
        [3, 1, 1, "D"]
    ]
    
    ruta_optima, min_distancia = optimizar_ruta_backtracking(pedidos, nodos)
    
    assert min_distancia == 30, f"Error: La distancia esperada era 30, pero fue {min_distancia}."
    nodos_ruta = [tramo[1] for tramo in ruta_optima]
    assert nodos_ruta == ["C", "B", "D"], "Error: La ruta debe sacrificar el inicio para minimizar la ruta."
    print("Test 2: [Ruta óptima] superado con éxito.\n")

def test_3_ruta_optima():
    """
    Comprueba un escenario con un camino de coste prohibitivo.
    Asegura que el algoritmo es capaz de lidiar con distancias extremas
    y encontrar el camino lógico.
    """
    print("Ejecutando Test 3: [Ruta óptima]")
    
    nodos = [
        {"origen": "A", "destino": "B", "distancia": 5},
        {"origen": "B", "destino": "C", "distancia": 5},
        {"origen": "C", "destino": "D", "distancia": 5},
        {"origen": "A", "destino": "D", "distancia": 1000}, # Rama a podar
        {"origen": "A", "destino": "C", "distancia": 100}
    ]
    pedidos = [
        [1, 1, 1, "B"],
        [2, 1, 1, "C"],
        [3, 1, 1, "D"]
    ]
    
    ruta_optima, min_distancia = optimizar_ruta_backtracking(pedidos, nodos)
    
    assert min_distancia == 15, f"Error: La distancia esperada era 15, pero fue {min_distancia}."
    assert len(ruta_optima) == 3, "Error: Debe componerse de 3 tramos."
    print("Test 3: [Ruta óptima] superado con éxito.\n")

def test_4_ruta_optima():
    """
    Prueba un grafo simétrico (un cuadrado) donde existen múltiples rutas
    con exactamente el mismo coste mínimo. Verifica que el algoritmo no falle
    al empatar.
    """
    print("Ejecutando Test 4: [Ruta óptima]")
    
    nodos = [
        {"origen": "A", "destino": "B", "distancia": 10},
        {"origen": "B", "destino": "C", "distancia": 10},
        {"origen": "C", "destino": "D", "distancia": 10},
        {"origen": "A", "destino": "D", "distancia": 10},
        {"origen": "A", "destino": "C", "distancia": 100},
        {"origen": "B", "destino": "D", "distancia": 100}
    ]
    pedidos = [
        [1, 1, 1, "B"],
        [2, 1, 1, "C"],
        [3, 1, 1, "D"]
    ]
    
    ruta_optima, min_distancia = optimizar_ruta_backtracking(pedidos, nodos)
    
    assert min_distancia == 30, f"Error: El perímetro suma 30, pero obtuvo {min_distancia}."
    nodos_ruta = [tramo[1] for tramo in ruta_optima]
    assert nodos_ruta in (["B", "C", "D"], ["D", "C", "B"]), "Error: Debe devolver uno de los perímetros válidos."
    print("Test 4: [Ruta óptima] superado con éxito.\n")

def test_5_ruta_optima():
    """
    Verifica que el algoritmo se comporta correctamente si se le pasa
    una lista de pedidos que van dirigidos al mismo punto de inicio ("A"),
    dejando la lista de destinos a visitar vacía.
    """
    print("Ejecutando Test 5: [Ruta óptima]")
    
    nodos = [
        {"origen": "A", "destino": "B", "distancia": 10}
    ]

    pedidos = [
        ["P1", 10, 50, "A"]
    ]
    
    ruta_optima, min_distancia = optimizar_ruta_backtracking(pedidos, nodos)
    
    assert min_distancia == 0, f"Error: La distancia debe ser 0, pero fue {min_distancia}."
    assert len(ruta_optima) == 0, "Error: La ruta detallada debe estar vacía porque no hay que moverse."
    print("Test 5: [Ruta óptima] superado con éxito.\n")


if __name__ == "__main__":
    test_1_ruta_optima()
    test_2_ruta_optima()
    test_3_ruta_optima()
    test_4_ruta_optima()
    test_5_ruta_optima()