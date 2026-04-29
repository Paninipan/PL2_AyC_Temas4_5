import random
import json
import string
"""
Funciones encargada de generar los escenarios.
Los escenarios tienen formato json:
    Pedidos
    Capacidad
    Nodos

Estructuras de datos:
        - Pedidos (Nx4 pedidos) :
            + Fila: Pedido
            + Columnas: id_pedido, peso, beneficio, destino

        - Capacidad de carga: C capacidad máxima de carga de vehículo.

        -Lista de tripletas entre puntos de entrega nodo:
            + Origen: Nombre del nodo
            + Destino: Nombre del nodo
            + Distancia: Distancia entre Or->Ds


Orden de generacion:
    1. Capacidad (int)
    2. Nodos (k nodos random [A-Z])
    3. Pedidos (destino = random from Nodos)
"""

def generar_escenario1(num_nodos, capacidad_maxima):
    # 1. Generar Capacidad (int)
    capacidad = random.randint(10, capacidad_maxima)

    # 2. Generar Nodos (k nodos random [A-Z])
    # Usamos string.ascii_uppercase para obtener letras de la A a la Z
    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]

    # Generar tripletas de distancias (Grafo completo para el ejemplo)
    nodos_data = []
    for i, origen in enumerate(nombres_nodos):
        for destino in nombres_nodos[i + 1:]:
            distancia = random.randint(5, 100)
            nodos_data.append({
                "origen": origen,
                "destino": destino,
                "distancia": distancia
            })

    # 3. Generar Pedidos (destino = random de nombres_nodos)
    pedidos_data = []
    for i in range(random.randint(1,5)):
        pedido = {
            "id_pedido": i + 1,
            "peso": random.randint(1, 500),
            "beneficio": random.randint(1, 500),
            "destino": random.choice(nombres_nodos)
        }
        pedidos_data.append(pedido)

    # Estructura final del JSON
    escenario = {
        "capacidad": capacidad,
        "nodos": nodos_data,
        "pedidos": pedidos_data
    }

    return json.dumps(escenario, indent=4)
def generar_escenario2(num_nodos, capacidad_max):
    # 1. Generar Capacidad (int)
    capacidad = random.randint(10, capacidad_max)

    # 2. Generar Nodos (k nodos random [A-Z])
    # Usamos string.ascii_uppercase para obtener letras de la A a la Z
    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]

    # Generar tripletas de distancias (Grafo completo para el ejemplo)
    nodos_data = []
    for i, origen in enumerate(nombres_nodos):
        for destino in nombres_nodos[i + 1:]:
            distancia = random.randint(5, 100)
            nodos_data.append({
                "origen": origen,
                "destino": destino,
                "distancia": distancia
            })

    # 3. Generar Pedidos (destino = random de nombres_nodos)
    pedidos_data = []
    for i in range(random.randint(50,200)):
        pedido = {
            "id_pedido": i + 1,
            "peso": random.randint(1, 5),
            "beneficio": random.randint(1, 500),
            "destino": random.choice(nombres_nodos)
        }
        pedidos_data.append(pedido)

    # Estructura final del JSON
    escenario = {
        "capacidad": capacidad,
        "nodos": nodos_data,
        "pedidos": pedidos_data
    }

    return json.dumps(escenario, indent=4)
def generar_escenario3(num_pedidos, num_nodos, capacidad_max):
    capacidad = random.randint(10, capacidad_max)

    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]

    nodos_data = []

    # Camino principal (A-B-C-D-...)
    for i in range(num_nodos - 1):
        d = random.randint(25, 28)
        nodos_data.append({
            "origen": nombres_nodos[i],
            "destino": nombres_nodos[i + 1],
            "distancia": d
        })

    # Atajos con coste parecido
    for i in range(num_nodos - 2):
        if random.random() < 0.5:
            d = random.randint(50, 55)  # parecido a 2 pasos
            nodos_data.append({
                "origen": nombres_nodos[i],
                "destino": nombres_nodos[i + 2],
                "distancia": d
            })

    # Pedidos
    pedidos_data = []
    for i in range(num_pedidos):
        pedidos_data.append({
            "id_pedido": i + 1,
            "peso": random.randint(1, 15),
            "beneficio": random.randint(10, 50),
            "destino": random.choice(nombres_nodos)
        })

    escenario = {
        "capacidad": capacidad,
        "nodos": nodos_data,
        "pedidos": pedidos_data
    }

    return json.dumps(escenario, indent=4)
def generar_escenario5(num_pedidos, num_nodos, capacidad_max):
    # 1. Generar Capacidad (int)
    capacidad = random.randint(10, capacidad_max)

    # 2. Generar Nodos (k nodos random [A-Z])
    # Usamos string.ascii_uppercase para obtener letras de la A a la Z
    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]

    # Generar tripletas de distancias (Grafo completo para el ejemplo)
    nodos_data = []
    for i, origen in enumerate(nombres_nodos):
        for destino in nombres_nodos[i + 1:]:
            distancia = random.randint(5, 100)
            nodos_data.append({
                "origen": origen,
                "destino": destino,
                "distancia": distancia
            })

    # 3. Generar Pedidos (destino = random de nombres_nodos)
    pedidos_data = []
    for i in range(num_pedidos):
        pedido = {
            "id_pedido": i + 1,
            "peso": random.randint(1, 15),
            "beneficio": random.randint(10, 50),
            "destino": random.choice(nombres_nodos)
        }
        pedidos_data.append(pedido)

    # Estructura final del JSON
    escenario = {
        "capacidad": capacidad,
        "nodos": nodos_data,
        "pedidos": pedidos_data
    }

    return json.dumps(escenario, indent=4)

# Ejemplo de uso:
escenario_json = generar_escenario5(num_pedidos=5, num_nodos=5, capacidad_max=50)
print(escenario_json)