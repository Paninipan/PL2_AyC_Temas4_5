from src.dp_seleccion import seleccion_pedidos

# Escenario 1: Escenario básico (Pocos pedidos N <= 5, grafo simple)

def test_escenario1_sobra_capacidad():
    """
    Prueba un escenario básico donde hay pocos pedidos y el vehículo
    tiene capacidad de sobra para llevarlos a todos.
    
    Objetivo: Verificar que el algoritmo no descarta pedidos erróneamente
    cuando no hay restricciones reales de peso.
    """
    print("Ejecutando Test Escenario 1.1: Capacidad de sobra")
   
    # Crear pedidos de prueba
    pedido_1 = [0, 10, 50, "A"]
    pedido_2 = [1, 20, 100, "B"]
    pedido_3 = [2, 30, 150, "C"]
    pedidos = [pedido_1, pedido_2, pedido_3]
    
    # Definición de capacidad y cálculo del subconjunto óptimo
    C = 100
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    
    # Verificar que el algoritmo funciona correctamente
    assert len(subconjunto_optimo) == 3, "Error: Debería haber seleccionado los 3 pedidos."
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    assert beneficio_total == 300, f"Error: El beneficio debería ser 300, pero fue {beneficio_total}"
    
    print("Test Escenario 1.1 superado con éxito.\n")


def test_escenario1_capacidad_limitada():
    """
    Prueba un escenario básico donde la capacidad es limitada y hay 
    que seleccionar una combinación específica de pedidos.
    
    Objetivo: Verificar que el algoritmo elige el subconjunto óptimo (maximizar beneficio)
    """
    print("Ejecutando Test Escenario 1.2: Selección óptima estricta")
    
    # Crear pedidos de prueba
    pedido_1 = [0, 5, 10, "A"]
    pedido_2 = [1, 4, 40, "B"]
    pedido_3 = [2, 6, 30, "C"]
    pedido_4 = [3, 3, 50, "D"]
    pedidos = [pedido_1, pedido_2, pedido_3, pedido_4]

    # Definición de capacidad y cálculo del subconjunto óptimo
    C = 10
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    
    # Verificar que el algoritmo funciona correctamente
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    ids_seleccionados = [p[0] for p in subconjunto_optimo]
    
    assert beneficio_total == 90, f"Error: El beneficio óptimo esperado es 90, pero se obtuvo {beneficio_total}."
    assert 1 in ids_seleccionados and 3 in ids_seleccionados, "Error: Debería haber seleccionado los IDs 1 y 3."
    assert len(subconjunto_optimo) == 2, "Error: Deberían haberse seleccionado exactamente 2 pedidos."
    
    print("Test Escenario 1.2 superado con éxito.\n")


def test_escenario1_capacidad_insuficiente():
    """
    Prueba un escenario básico donde un pedido individual supera
    por sí solo la capacidad total del vehículo.
    
    Objetivo: Asegurar que el algoritmo filtra correctamente los objetos 
    que no caben y no rompe la restricción de peso máximo.
    """
    print("Ejecutando Test Escenario 1.3: Pedido demasiado pesado")

    # Crear pedidos de prueba
    pedido_1 = [0, 50, 200, "A"]    # Excede la capacidad (50 > 20)
    pedido_2 = [1, 15, 100, "B"]    # Cabe en el vehículo
    pedidos = [pedido_1, pedido_2]

    # Definición de capacidad y cálculo del subconjunto óptimo
    C = 20
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    
    # Verificar que el algoritmo funciona correctamente
    assert len(subconjunto_optimo) == 1, "Error: Solo debería coger 1 pedido."
    assert subconjunto_optimo[0][0] == 1, "Error: Debería haber cogido el pedido con ID 1."
    assert subconjunto_optimo[0][2] == 100, "Error: El beneficio debería ser 100."
    
    print("Test Escenario 1.3 superado con éxito.\n")


# Escenario 2: Capacidad Crítica (Muchos pedidos pequeños -> fuerza la DP)

def test_escenario2_fallo_voraz():
    """
    Prueba un escenario donde un algoritmo voraz fallaría, forzando a
    la Programación Dinámica a evaluar combinaciones para hallar el óptimo.
    
    Objetivo: Demostrar que la DP encuentra la combinación perfecta llenando
    la capacidad con pedidos más pequeños en lugar de coger el de mayor beneficio.
    """
    print("Ejecutando Test Escenario 2.1: Fallo al utilizar un algoritmo voraz")
    
    # Crear pedidos de prueba
    pedido_1 = [0, 6, 10, "A"]      # Mayor ratio beneficio/peso, pero deja 4kg vacíos.
    pedido_2 = [1, 5, 8, "B"]
    pedido_3 = [2, 5, 8, "C"]
    pedidos = [pedido_1, pedido_2, pedido_3]
    
    # Definición de capacidad y cálculo del subconjunto óptimo
    C = 10
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    
    # Verificar que el algoritmo funciona correctamente
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    ids_seleccionados = [p[0] for p in subconjunto_optimo]
    
    # El subconjunto óptimo es llevar los pedidos 2 (Peso 5, Bº 8) y 3 (Peso 5, Bº 8) 
    # Peso total = 10, Beneficio total = 16
    assert beneficio_total == 16, f"Error: El beneficio óptimo esperado es 16, pero se obtuvo {beneficio_total}."
    assert 1 in ids_seleccionados and 2 in ids_seleccionados, "Error: Debería haber seleccionado los IDs 1 y 2."
    assert len(subconjunto_optimo) == 2, "Error: Deberían haberse seleccionado exactamente 2 pedidos."
    
    print("Test Escenario 2.1 superado con éxito.\n")


def test_escenario2_muchos_pedidos():
    """
    Prueba un escenario con muchos pedidos de peso y beneficio variable, 
    forzando a la caché de la DP a recorrer múltiples opciones.
    
    Objetivo: Verificar el rendimiento y la exactitud en la toma de decisiones 
    con una número mayor de posibilidades.
    """
    print("Ejecutando Test Escenario 2.2: Muchos pedidos pequeños")
    
    # Crear pedidos de prueba
    pedido_1 = [0, 1, 2, "A"]
    pedido_2 = [1, 2, 5, "B"]
    pedido_3 = [2, 3, 8, "C"]
    pedido_4 = [3, 4, 11, "D"]
    pedido_5 = [4, 5, 15, "E"]
    pedido_6 = [5, 6, 17, "F"]
    pedido_7 = [6, 7, 20, "G"]
    pedidos = [pedido_1, pedido_2, pedido_3, pedido_4, pedido_5, pedido_6, pedido_7]
    
    # Definición de capacidad y cálculo del subconjunto óptimo
    C = 12
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    
    # Verificar que el algoritmo funciona correctamente
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    ids_seleccionados = [p[0] for p in subconjunto_optimo]
    
    # El subconjunto óptimo es el pedido 5 (Peso 5, Bº 15) y el pedido 7 (Peso 7, Bº 20)
    # Peso total = 12, Beneficio total = 35
    assert beneficio_total == 35, f"Error: El beneficio óptimo esperado es 35, pero se obtuvo {beneficio_total}."
    assert 4 in ids_seleccionados and 6 in ids_seleccionados, "Error: Debería haber seleccionado los IDs 4 y 6."
    assert len(subconjunto_optimo) == 2, "Error: Deberían haberse seleccionado exactamente 2 pedidos."
    
    print("Test Escenario 2.2 superado con éxito.\n")


def test_escenario2_capacidad_minima():
    """
    Prueba un escenario con muchos pedidos pero con una capacidad de vehículo 
    muy restrictiva.
    
    Objetivo: Validar que la recursividad base de la DP actúa correctamente y
    selecciona solo los pedidos más valiosos sin pasarse del límite.
    """
    print("Ejecutando Test Escenario 2.3: Muchos pedidos con capacidad restrictiva")
    
    # Crear pedidos de prueba
    pedido_1 = [0, 4, 100, "A"]     # Muy valioso, pero no cabe
    pedido_2 = [1, 5, 120, "B"]     # Muy valioso, pero no cabe
    pedido_3 = [2, 1, 10, "C"]
    pedido_4 = [3, 2, 25, "D"]
    pedido_5 = [4, 1, 12, "E"]
    pedidos = [pedido_1, pedido_2, pedido_3, pedido_4, pedido_5]
    
    # Definición de capacidad y cálculo del subconjunto óptimo
    C = 3
    subconjunto_optimo = seleccion_pedidos(pedidos, C)
    
    # Verificar que el algoritmo funciona correctamente
    beneficio_total = sum(p[2] for p in subconjunto_optimo)
    ids_seleccionados = [p[0] for p in subconjunto_optimo]
    
    # El subconjunto óptimo es el pedido 4 (Peso 2, Bº 25) y pedido 5 (Peso 1, Bº 12).
    # Peso total = 3, Beneficio total = 37.
    assert beneficio_total == 37, f"Error: El beneficio esperado es 37, pero se obtuvo {beneficio_total}."
    assert 3 in ids_seleccionados and 4 in ids_seleccionados, "Error: Debería haber seleccionado los IDs 3 y 4."
    
    print("Test Escenario 2.3 superado con éxito.\n")


if __name__ == '__main__':

    # Tests Escenario 1
    test_escenario1_sobra_capacidad()
    test_escenario1_capacidad_limitada()
    test_escenario1_capacidad_insuficiente()
    
    # Tests Escenario 2
    test_escenario2_fallo_voraz()
    test_escenario2_muchos_pedidos()
    test_escenario2_capacidad_minima()
    