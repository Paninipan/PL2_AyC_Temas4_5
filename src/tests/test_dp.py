from dp_seleccion import seleccion_pedidos

def test_1_seleccion_pedidos():
    """
    Demuestra que el algoritmo utiliza la Programación Dinámica y no se queda
    con el mejor ratio beneficio/peso si eso perjudica el total, como podría llegar
    a hacer un algoritmo voraz.
    """
    print("Ejecutando Test 1: [Seleccion de pedidos]")
    
    # El primer pedido tiene mejor ratio (7/6 = 1.16), pero si lo coges, 
    # te quedas con 4 de capacidad y no puedes meter nada más.
    # La solución óptima es escoger los pedidos 2 y 3 (Beneficio total = 10).

    pedidos = [
        [1, 6, 7, "A"],
        [2, 5, 5, "B"],
        [3, 5, 5, "C"]
    ]

    C = 10  # Capacidad máxima
    
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    
    assert beneficio_total == 10, f"Error: El beneficio esperado era 10 , pero fue {beneficio_total}."
    assert len(subconjunto_optimo) == 2, "Error: Debería haber seleccionado 2 pedidos exactos."
    print("Test 1: [Selección de pedidos] superado con éxito.\n")

def test_2_seleccion_pedidos():
    """
    Comprueba los límites de los índices y sumas asegurando que el algoritmo
    selecciona pedidos exactamente hasta su máxima capacidad sin pasarse.
    """
    print("Ejecutando Test 2: [Seleccion de pedidos]")
    
    pedidos = [
        [1, 5, 10, "A"],
        [2, 10, 20, "B"],
        [3, 2, 1, "C"]      # Este pedido no debería entrar
    ]

    C = 15  # Capacidad máxima
    
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    peso_total = sum(p[1] for p in subconjunto_optimo)
    
    assert beneficio_total == 30, f"Error: El beneficio esperado era 30, pero fue {beneficio_total}"
    assert peso_total == 15, f"Error: El peso total {peso_total} debería ser la capacidad máxima de {C}."
    assert len(subconjunto_optimo) == 2, "Error: Debería haber seleccionado los pedidos 1 y 2."
    print("Test 2: [Seleccion de pedidos] superado con éxito.\n")

def test_3_seleccion_pedidos():
    """
    Verifica que el algoritmo se comporta bien y devuelve 
    listas vacías cuando es imposible transportar ningún pedido.
    """
    print("Ejecutando Test 3: [Seleccion de pedidos]")
    
    pedidos = [
        [1, 10, 50, "A"],
        [2, 6, 20, "B"]
    ]
    C = 5   # Capacidad inferior a cualquier pedido
    
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    
    assert len(subconjunto_optimo) == 0, "Error: La lista de pedidos seleccionados debería estar vacía."
    assert beneficio_total == 0, f"Error: El beneficio debería ser 0, pero fue {beneficio_total}"
    print("Test 3: [Seleccion de pedidos] superado con éxito.\n")

def test_4_seleccion_pedidos():
    """
    Comprueba cómo el algoritmo actúa cuando hay dos pedidos 
    idénticos pero solo hay capacidad para uno.
    """
    print("Ejecutando Test 4: [Seleccion de pedidos]")
    
    pedidos = [
        [1, 10, 100, "A"],
        [2, 10, 100, "A"]
    ]

    C = 10  # Capacidad máxima
    
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    
    assert beneficio_total == 100, f"Error: El beneficio esperado era 100, pero fue {beneficio_total}"
    assert len(subconjunto_optimo) == 1, "Error: Solo hay espacio para 1 pedido, no para ambos."
    print("Test 4: [Seleccion de pedidos] superado con éxito.\n")

def test_5_seleccion_pedidos():
    """
    Comprueba la inicialización de la relación de recurrencia con
    una capacidad enorme pero una matriz de pedidos vacía.
    """
    print("Ejecutando Test 5: [Seleccion de pedidos]")
    
    pedidos = []
    C = 100
    
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    
    assert len(subconjunto_optimo) == 0, "Error: Debería devolver una lista vacía."
    print("Test 5: [Seleccion de pedidos] superado con éxito.\n")


if __name__ == "__main__":
    test_1_seleccion_pedidos()
    test_2_seleccion_pedidos()
    test_3_seleccion_pedidos()
    test_4_seleccion_pedidos()
    test_5_seleccion_pedidos()
    