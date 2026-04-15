"""
Este es el modulo principal de la aplicacion, este contiene:
    La funcion main encargada de llamar a las demas funciones y ejecutar el programa.
    ...
    
"""

"""
Estructuras de datos y algoritmos implementados:

    Estructuras de datos:
        - Matriz de pedidos (Nx3 pedidos) :
            + Fila: Pedido 
            + Columnas: id_pedido, peso, beneficio
        
        - Capacidad de carga: C (entero) representando la capacidad máxima de carga de cada vehículo.

        - Diccionario de camiones y pedidos asignados: ???
            + Clave: id_camion 
            + Valor: Tupla "Tripelata -> + punto de entrega"
                * Beneficio total
                * Lista de pedidos asignados a ese camión.
        
        - Matriz de distancias entre puntos de entrega (grafo ponderado) {k*k nodos}:
            + Fila: Punto o nodo de entrega
            + Columna: Distancia a otro nodo
        
        - Lista de entregas (longitud k nodos):
            + Nodo de entrega 
   
    Algoritmos:
        - Selección de pedidos (Programación Dinámica)
        - Backtracking para encontrar la ruta óptima 
"""


def main():
    print("Hello, World!")



if __name__ == "__main__":
    main()