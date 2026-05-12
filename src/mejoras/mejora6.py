from dp_seleccion import seleccion_pedidos

def capacidad_minima_para_beneficio(pedidos, capacidad_maxima, porcentaje_objetivo):
    """
    Calcula la capacidad mínima (C) necesaria del vehículo para alcanzar un % 
    de beneficio objetivo establecido.
    """
    # Si no hay pedidos o la capacidad máxima no es mayor que 0, retornamos 0
    if not pedidos or capacidad_maxima <= 0:
        return 0

    # 1. Calculamos el beneficio máximo posible usando toda la capacidad
    pedidos_seleccionados = seleccion_pedidos(pedidos, capacidad_maxima)
    beneficio_max_posible = sum(p[2] for p in pedidos_seleccionados)
    
    beneficio_objetivo = beneficio_max_posible * (porcentaje_objetivo / 100.0)

    # 2. Búsqueda binaria de la mínima capacidad
    limite_inferior = 0
    limite_superior = capacidad_maxima
    capacidad_minima = capacidad_maxima

    while limite_inferior <= limite_superior:
        capacidad_prueba = (limite_inferior + limite_superior) // 2
        
        # Simulamos la selección con la capacidad de prueba
        subconjunto = seleccion_pedidos(pedidos, capacidad_prueba)
        beneficio_obtenido = sum(p[2] for p in subconjunto)

        if beneficio_obtenido >= beneficio_objetivo:
            # Si alcanzamos el objetivo, guardamos la capacidad y buscamos si podemos con menos
            capacidad_minima = capacidad_prueba
            limite_superior = capacidad_prueba - 1
        else:
            # Si no alcanzamos el objetivo, necesitamos más capacidad.
            limite_inferior = capacidad_prueba + 1

    return capacidad_minima

# --- Prueba de Mejora 6: Búsqueda binaria en optimización ---

# Pedidos
pedido1 = [1, 2, 10, "A"]
pedido2 = [2, 3, 20, "B"]
pedido3 = [3, 5, 30, "C"]

pedidos = [pedido1, pedido2, pedido3]
C = 10

# Caso 1: Queremos el 50% del beneficio (Beneficio total = 60, el 50% es 30).
# Con capacidad 5 podemos llevar el pedido3 y ganar 30.
print("Capacidad para 50% de beneficio (Debería ser 5):")
print(capacidad_minima_para_beneficio(pedidos, C, 50))

# Caso 2: Queremos el 80% del beneficio (Beneficio objetivo = 48).
# Necesitamos coger pedido2 y pedido3 (beneficio 50, peso conjunto 8).
print("\nCapacidad para 80% de beneficio (Debería ser 8):")
print(capacidad_minima_para_beneficio(pedidos, C, 80))

# Caso 3: Queremos el 100% del beneficio.
# Hay que llevarse todo el peso.
print("\nCapacidad para 100% de beneficio (Debería ser 10):")
print(capacidad_minima_para_beneficio(pedidos, C, 100))