import dp_seleccion
from generador_escenarios import *
from backtracking_ruta import *
from dp_seleccion import *
"""
Este es el modulo principal de la aplicacion, este contiene:
    La funcion main encargada de llamar a las demas funciones y ejecutar el programa.
    ...

Estructuras de datos y algoritmos implementados:

    Estructuras de datos:
        - Matriz de pedidos (Nx4 pedidos) :
            + Fila: Pedido 
            + Columnas: id_pedido, peso, beneficio, destino
        
        - Capacidad de carga: C capacidad máxima de carga de vehículo.

        -Lista de pedidos asignados:
            + Valor: Tupla 3 valors
                * Id_Pedido
                * Destino
                * Beneficio
        
        -Lista de tripletas entre puntos de entrega nodo:
            + Origen: Nombre del nodo
            + Destino: Nombre del nodo
            + Distancia: Distancia entre Or->Ds
        
        - Lista de entregas (longitud max k nodos):
            + Nodo de entrega
   
    Algoritmos:
        - Selección de pedidos (Programación Dinámica)
        - Backtracking para encontrar la ruta óptima 
"""
def validar_escenario():
    num = int(input("Elige escenario (1-5): "))
    valido = False
    while not valido:
        if num < 1 or num > 5:
            print("Número inválido")
            num = int(input("Elige escenario(1-5): "))
        else:
            valido = True
    return num

"""
Funcion encargada de generar el escenario pedido según la opcion
puede necesitar:
    +num_nodos
    +capadidad_max
    +num_pedidos
"""
def seleccion_escenario(num):
    num_nodos = int(input("Elige numero de nodos: "))
    capacidad = int(input("Elige capacidad maxima del camion: "))
    if num == 1:
        return generar_escenario1(num_nodos, capacidad)
    elif num == 2:
        return generar_escenario1(num_nodos, capacidad)
    elif num == 3:
        num_pedidos = int(input("Elige numero de pedidos: "))
        return generar_escenario3(num_pedidos, num_nodos, capacidad)
    #elif num == 4:
        return generar_escenario4()
    else:
        num_pedidos = int(input("Elige numero de pedidos: "))
        return generar_escenario5(num_pedidos, num_nodos, capacidad)


def main():
    print("1. Generar nuevo escenario")
    print("2. Usar escenario existente")

    opcion = int(input("Elige una opción: "))
    salir = False
    while (not salir):
        if opcion < 1 or opcion > 2:
            print("Número inválido")
            opcion = int(input("Elige una opción: "))
        else:
            salir = True

    if opcion == 1:
        num = validar_escenario()

        json_generado = seleccion_escenario(num)

        nombre = f"escenario{num}.json"

        ruta = guardar_json(json_generado, nombre)

        print(f"Escenario {num} generado en: {ruta}")

        datos = leer_json_a_diccionario(ruta)

    elif opcion == 2:
        num = validar_escenario()

        ruta = os.path.join("data/escenarios", f"escenario{num}.json")

        if not os.path.exists(ruta):
            print("Ese escenario no existe todavía")
            return

        datos = leer_json_a_diccionario(ruta)

    else:
        print("Opción no válida")
        return

    #Estructura de datos
        # print(datos["capacidad"])
        # print(datos["nodos"])
        # print(datos["pedidos"])

    pedidos = datos["pedidos"]
    capacidad = datos["capacidad"]

    pedidos_seleccionados = seleccion_pedidos(pedidos, capacidad)
    imprimir_camion(pedidos_seleccionados)

    nodos = datos["nodos"]
    ruta = optimizar_ruta_backtracking(pedidos_seleccionados, nodos, None)
    imprimir_nodos(ruta,nodos)



if __name__ == "__main__":
    main()