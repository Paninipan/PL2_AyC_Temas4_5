"""
Este módulo contiene la función de seleccion de pedidos segun:
    -Cada pedido se representa como una estructura: 
        + Pedido = (id, peso, beneficio) 
    -Entradas: 
        + Una lista de pedidos disponibles. 
        + Una capacidad máxima de carga C. 
    -Se debe seleccionar el subconjunto de pedidos que: 
        + No exceda C. 
        + Maximice el beneficio total.
        + Salida:
            + Diccionario:
                + Clave: id_camion
                + Valor: Tupla "Tripelata -> + punto de entrega"??
                    * Beneficio total
                    * Lista de pedidos asignados a ese camión.

Solucion realizada medienate Programación Dinámica, descente recursivo.
"""

def seleccion_pedidos(pedidos, capacidad) -> dict:
    
    def seleccion_pedidos_cache(pedidos, capacidad, cache):
        if len(pedidos) == 0 or capacidad <= 0:
            return 0, []
        if pedidos == None:
            return 0, []
    

    return diccionario_entregas