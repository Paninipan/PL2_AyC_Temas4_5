import sys

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

import random
import json
import os
import string

def generar_escenario1(num_nodos, capacidad_max):
    capacidad = capacidad_max
    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]

    nodos_data = []
    for i, origen in enumerate(nombres_nodos):
        for destino in nombres_nodos[i + 1:]:
            distancia = random.randint(2, 10)
            nodos_data.append({"origen": origen, "destino": destino, "distancia": distancia})

    # Pedidos como tuplas: (id, peso, beneficio, destino)
    pedidos_data = []
    for i in range(random.randint(1, 5)):
        pedido = (
            i + 1,                          # id_pedido
            random.randint(1, 20),         # peso
            random.randint(1, 500),         # beneficio
            random.choice(nombres_nodos)    # destino
        )
        pedidos_data.append(pedido)

    for nodo in nodos_data:
        if 1 == random.randint(1, 5):
            nodo["tmin"] = random.randint(0, 4)
            nodo["tmax"] = random.randint(5, 10) *( len(nodos_data)/2)
        else:
            nodo["tmin"] = 0
            nodo["tmax"] = sys.maxsize

    escenario = {"capacidad": capacidad, "nodos": nodos_data, "pedidos": pedidos_data}
    return json.dumps(escenario, indent=4)

def generar_escenario2(num_nodos, capacidad_max):
    capacidad = capacidad_max
    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]

    nodos_data = []
    for i, origen in enumerate(nombres_nodos):
        for destino in nombres_nodos[i + 1:]:
            distancia = random.randint(2, 10)
            nodos_data.append({"origen": origen, "destino": destino, "distancia": distancia})

    # Pedidos como tuplas: (id, peso, beneficio, destino)
    pedidos_data = []
    for i in range(random.randint(50, 200)):
        pedido = (
            i + 1,
            random.randint(1, 5),
            random.randint(1, 500),
            random.choice(nombres_nodos)
        )
        pedidos_data.append(pedido)

    for nodo in nodos_data:
        if 1 == random.randint(1, 5):
            nodo["tmin"] = random.randint(0, 4)
            nodo["tmax"] = random.randint(5, 10) *( len(nodos_data)/2)
        else:
            nodo["tmin"] = 0
            nodo["tmax"] = sys.maxsize


    escenario = {"capacidad": capacidad, "nodos": nodos_data, "pedidos": pedidos_data}
    return json.dumps(escenario, indent=4)

def generar_escenario3(num_pedidos, num_nodos, capacidad_max):
    capacidad = capacidad_max
    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]
    nodos_data = []

    for i in range(num_nodos - 1):
        nodos_data.append({"origen": nombres_nodos[i], "destino": nombres_nodos[i + 1], "distancia": random.randint(25, 28)})

    for i in range(num_nodos - 2):
        nodos_data.append({"origen": nombres_nodos[i], "destino": nombres_nodos[i + 2], "distancia": random.randint(50, 55)})

    # Pedidos como tuplas: (id, peso, beneficio, destino)
    pedidos_data = []
    for i in range(num_pedidos):
        pedido = (
            i + 1,
            random.randint(1, 15),
            random.randint(10, 50),
            random.choice(nombres_nodos)
        )
        pedidos_data.append(pedido)
    for nodo in nodos_data:
        nodo["tmin"] = 0
        nodo["tmax"] = sys.maxsize

    escenario = {"capacidad": capacidad, "nodos": nodos_data, "pedidos": pedidos_data}
    return json.dumps(escenario, indent=4)

def generar_escenario4(num_nodos, capacidad_max):
    capacidad = capacidad_max
    nodos = list(string.ascii_uppercase)[:num_nodos]

    origen = nodos[0]
    destinos = nodos[1:]

    camino_optimo = [origen] + destinos

    nodos_data = []
    tiempo = 0

    # construir camino óptimo con tiempos consistentes
    for i in range(len(camino_optimo) - 1):
        o = camino_optimo[i]
        d = camino_optimo[i + 1]

        tiempo += 1

        nodos_data.append({
            "origen": o,
            "destino": d,
            "distancia": 1,
            "tmin": tiempo,
            "tmax": tiempo
        })


    for i in range(len(nodos)):
        for j in range(i + 1, len(nodos)):

            o = nodos[i]
            d = nodos[j]

            # evitar duplicar aristas del óptimo
            if (o, d) in zip(camino_optimo, camino_optimo[1:]):
                continue

            nodos_data.append({
                "origen": o,
                "destino": d,
                "distancia": 10 + random.randint(1, 5),
                "tmin": 0,
                "tmax": sys.maxsize
            })

    pedidos = []
    for i, nodo in enumerate(destinos):
        pedidos.append((
            i + 1,
            random.randint(1, 10),
            random.randint(100, 500),
            nodo
        ))

    escenario = {
        "capacidad": capacidad,
        "nodos": nodos_data,
        "pedidos": pedidos,
    }
    return json.dumps(escenario, indent=4)

def generar_escenario5(num_pedidos, num_nodos, capacidad_max):
    capacidad =  capacidad_max
    nombres_nodos = list(string.ascii_uppercase)[:num_nodos]
    nodos_data = []

    for i, origen in enumerate(nombres_nodos):
        for destino in nombres_nodos[i + 1:]:
            distancia = random.randint(2, 10)
            nodos_data.append({"origen": origen, "destino": destino, "distancia": distancia})

    # Pedidos como tuplas: (id, peso, beneficio, destino)
    pedidos_data = []
    for i in range(num_pedidos):
        pedido = (
            i + 1,
            random.randint(1, 15),
            random.randint(10, 50),
            random.choice(nombres_nodos)
        )
        pedidos_data.append(pedido)

    escenario = {"capacidad": capacidad, "nodos": nodos_data, "pedidos": pedidos_data}

    for nodo in nodos_data:
        if 1 == random.randint(1, 5):
            nodo["tmin"] = random.randint(0, 4)
            nodo["tmax"] = random.randint(5, 10) *( len(nodos_data)/2)
        else:
            nodo["tmin"] = 0
            nodo["tmax"] = sys.maxsize

    return json.dumps(escenario, indent=4)

def guardar_json(archivo_json, nombre_archivo):
    ruta_carpeta = "data/escenarios"

    # Crear carpeta si no existe
    os.makedirs(ruta_carpeta, exist_ok=True)

    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

    with open(ruta_completa, 'w', encoding='utf-8') as f:
        f.write(archivo_json)

    return ruta_completa

def leer_json_a_diccionario(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)  # ← convierte a dict automáticamente

    return datos
