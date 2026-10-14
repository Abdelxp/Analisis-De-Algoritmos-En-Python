#Algoritmo de ordenamiento burbuja
"""
1.Recorrer la lista varias veces(i)
2.En cada pasada,comparar los elementos consecutivos
3.Si el de la izquierda es mayor que el de la derecha,intercambiarlos
4.Al final de cada repeticion, el mayor va a quedar en la derecha
"""
def ordenamiento_burbuja(lista):
    n=len(lista)
    print(f"Cantidad de elementos en la lista: {n}")
    for i in range(n-1):
        print(f"\n --- i={i}---")
        for j in range(n-1-i):
            print(f"\n --- j={j}---")
            print(f"Comparar({lista[j]}) > ({lista[j+1]})")
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                print(f"Nuevos: {lista[j]},{lista[j+1]}")
            print(f"Nueva lista:j={j}: {lista}")     
    return lista
         
tiempos_espera=[15,5,12,3,9];
print(f"Tiempos de espera(orig): {tiempos_espera}")
tiempos_ordenados=ordenamiento_burbuja(tiempos_espera.copy())
print(f"Tiempos de espera(ord): {tiempos_ordenados}")
