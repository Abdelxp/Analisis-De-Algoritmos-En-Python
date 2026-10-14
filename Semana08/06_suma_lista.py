#Sumar elementos de una lista
"""
cadena= "recursivo"
cadena[-1] # "o"
cadena[:-1] # "recursiv"
cadena[1:] # todo menos el primero
cadena[inicio,fin] 
inicio-->indice donde se inicia (por defecto 0)
fin-->indice hasta el cual cortar,sin incluirse
negativo-->cuenta desde la posicion final de la cadena

"""
def suma(lista): #[2,4,6]
    # Caso Base
    print(f"Iniciamos con: {lista}")
    if len(lista)== 0:
        print("Caso Base: retornar 0")
        return 0
    else:
        # Caso Recursivo
        return lista[0] + suma(lista[1:])
        # 2 + suma([4,6]) = 2 + [esperando](10)=12
        # 4 + suma([6]) = 4 + [esperando](6)=10
        # 6 + suma([]) = 6 + 0
print(f"Suma de elementos de una lista es: {suma([2,4,6])}")