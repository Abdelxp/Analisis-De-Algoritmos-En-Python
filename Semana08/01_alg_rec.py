"""
Es una funcion que se llama asi misma.

Componentes:
1.Caso Base
2.Caso Recursivo

Nota:Los valores se van guardando en la pila de llamadas (stack).
Ejemplo de estructura de una funcion recursiva:
def funcion_recursiva(parametro):
    # Caso Base
    if condicion _base== 0:
        return resultado_base
    else:
        # Caso Recursivo
        return funcion_recursiva* (parametro_siguiente)

"""
def cuenta_regresiva(n):
    # Caso Base
    if n== 0:
        print("Despegue!!!")
    else:
        # Caso Recursivo
        print(f"Iniciando cuenta regresiva: {n}")
        cuenta_regresiva(n-1)
cuenta_regresiva(5) 
      