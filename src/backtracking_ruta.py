"""
Este módulo contiene la función de backtracking para encontrar la ruta óptima según:

    Una vez seleccionados los pedidos: 
        + Cada pedido tiene un punto de entrega. 
        + La ciudad se modela como un grafo ponderado (matriz o lista de adyacencia). 
    Se debe encontrar el orden de entrega que minimice la distancia total. 
    
    Restricciones adicionales: 
        + Ventanas de tiempo máximas por pedido (opcional pero valorable). 
    
    Se deben implementar estrategias de poda:
        + por distancia acumulada
        + tiempo excedido, etc.). 

    Requisito obligatorio: 
        + El algoritmo debe usar backtracking explícito, no heurísticas voraces.
"""