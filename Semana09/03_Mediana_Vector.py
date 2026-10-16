#Mediana de un vector
"""
El valor del centro de un vector ORDENADO

1. Si la cantidad de valores es IMPAR, la mediana es el medio
2. Si la cantidad de valores es PAR, la mediana es el promedio de los dos centrales

IMPAR
vector_original=[7,1,5]
vector_ordenado=[1,5,7]
indice_centro=len(vector_ordenado)//2 = 3//2 = 1
Mediana= 5

PAR
vector_original=[7,1,5,3]
vector_ordenado=[1,3,5,7]
indice_centro_1=len(vector_ordenado)//2 = 4//2 = 2
indice_centro_2=indice_centro_1 -1
mediana = (5+3)/2 = 8/2 = 4

ESTRATEGIA
1. Ordenar los valores
2. Calcular la cantidad de valores(len)
3. Indicar si es par o impar
4. Calcular los índices medios
5. Calcular el valor de la mediana

"""
def mediana(vector):
    print(f"Vector original: {vector}")
    #sort != soted
    vector_ordenado=sorted(vector)
    print(f"Vector ordenado: {vector_ordenado}")
    n=len(vector_ordenado)
    if n % 2 == 1: #impar
        mediana=vector_ordenado[n//2]
        print(f"IMPAR n ={n} , Mediana esta en el indice{n//2}")
    else:
        medio_1=vector_ordenado[n//2]
        medio_2=vector_ordenado[n//2-1]
        mediana= (medio_1 + medio_2) / 2
        print(f"PAR n = {n} , Mediana es el promedio de {medio_1} y {medio_2}")
    print(f"Mediana calculada: {mediana}")
    return mediana

vector_original=[7,1,5,3]
print(mediana(vector_original))

