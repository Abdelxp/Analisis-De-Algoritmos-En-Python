#Búsqueda binaria
"""
--> Solo funciona si la lista está ordenada de forma creciente
1. Tomamos el elemento del medio (// división entera)
2. Si es el elemento que busco, entonces Fin.
3. Si el objetivo es menor, seguir buscando en la mitad izquierda.
4. Si el objetivo es mayor, seguir buscando en la mitad derecha.
"""
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
def busqueda_binaria(lista, objetivo):
    print(f"Lista: {lista}, BUSCAR objetivo: {objetivo}")
    izquierda = 0
    derecha = len(lista) - 1 
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 # (0 + 5) // 2 = 2
        valor_medio = lista[medio] # 8
        print(f"Índice medio: {medio}, con el valor: {valor_medio}")
        if valor_medio == objetivo:
            print("--> Encontrado en el medio")
            return medio
        elif objetivo < valor_medio:
            derecha = medio - 1
            print(f"Límites: izquierda: {izquierda}, derecha: {derecha}")
        else:
            izquierda = medio + 1
            print(f"Límites: izquierda: {izquierda}, derecha: {derecha}")
    print("No se encontró el elemento")
    return -1

# Lista inicial desordenada
lista = [8, 12, 4, 10, 6, 14]
objetivo = 12

# Se ordena la copia de la lista y se pasa a la búsqueda binaria
lista_ordenada = ordenamiento_burbuja(lista.copy())
busqueda_binaria(lista_ordenada, objetivo)