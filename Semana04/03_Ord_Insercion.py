#Algoritmo de ordenamiento insercion
"""
[15,5,12,3,9]
1.Comparar el 15 con el 5 [5,15,12,3,9]
2.El 12, insertamos entre el 5 y el 15 [5,12,15,3,9]
3.El 3, lo insertamos antes del 5 [3,5,12,15,9]
4.El 9, lo insertamos entre el 5 y el 12 [3,5,9,12,15]

"""
def ordenamiento_insercion(lista):
    n=len(lista)
    print(f"Cantidad de elementos en la lista: n= {n}")
    for i in range(1,n):
        print("="*50)
        print(f"\n --- i={i}---")
        valor_actual=lista[i]
        posicion=i-1 #->15
        print(f"Valor actual={valor_actual}")
        print(f"Comparar desde la posicion={posicion}")
        print(f"Estado de lista: {lista}")
        while posicion>=0 and lista[posicion]>valor_actual:
            print (f"Comparar({lista[posicion]}) > ({valor_actual})")
            print(f"Desplazamos {lista[posicion]} a la derecha (posicion={posicion+1})")
            lista[posicion+1]=lista[posicion]
            print(f"-----> Lista Actual: {lista}")
            posicion-=1
            lista[posicion+1]=valor_actual
            print(f"Insertamos {valor_actual} en la posicion={posicion+1}")
            print(f"Nueva lista: {lista}")
    return lista
           

tiempos_espera=[15,5,12,3,9];
print(f"Tiempos de espera(orig): {tiempos_espera}")
tiempos_ordenados=ordenamiento_insercion(tiempos_espera.copy())
print(f"Tiempos de espera(ord): {tiempos_ordenados}")