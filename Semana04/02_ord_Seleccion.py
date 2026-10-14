#Algoritmo de ordenamiento selección
"""
1.Suponer que el primer elemento es el menor
2Comparemos con todos para encontrar el menor
3.Colocamos el menor a la izquierda

"""
def ordenamiento_seleccion(lista):
    n=len(lista)
    print(f"Cantidad de elementos en la lista: n= {n}")
    for i in range(n-1):
        print(f"\n --- i={i}---")
        min_index=i
        print(f"min_index={i}")
        for j in range(i+1,n):
            print(f"\n ===j={j}===")
            print(f"Comparamos ({lista[j]}) < ({lista[min_index]})")
            if lista[j]<lista[min_index]:
                min_index=j
                print(f"Nuevo min_index={min_index}")
        if  min_index!=i:
            lista[i],lista[min_index]=lista[min_index],lista[i]
        print(f"Nueva lista:i={i}: {lista}")
    return lista
tiempos_espera=[15,5,12,3,9];
print(f"Tiempos de espera(orig): {tiempos_espera}")
tiempos_ordenados=ordenamiento_seleccion(tiempos_espera.copy())
print(f"Tiempos de espera(ord): {tiempos_ordenados}")