#Algortimo de dijkstra
"""
Encuentra la distancia mas corta desde un lado origen 
los pasos de las aristas deben ser positivos}
¿Que nesecitamos?
1. Grafo(nodos,aristas con pesos)
2.Un nodo de inicio
3.Una estructura para guardar los pesos minimos encontrados

"""
import heapq
def alg_dijkstra(grafo,inicio):
    print(f"Grafo: {grafo}")
    distancias = {} #diccionarios {} != listas []
    for nodo in grafo:
        distancias[nodo]=float('inf')
    print(f"Distancias: {distancias}")
    distancias[inicio]=0
    print(f"Distancias: {distancias}")
    heap=[(0,inicio)]
    print(f"Nodo de inicio: {inicio}")
    while heap:
        distancia_actual, nodo_actual = heapq.heappop(heap)
        print(f"\n--->Visitando nodo: {nodo_actual} con distancia actual: {distancia_actual}")
        for vecino, peso in grafo[nodo_actual]:
            print(f"\nVecino: {vecino} con peso {peso}")
            nueva_distancia = distancia_actual + peso
            print(f"Verificar {vecino} con peso {peso} acumula Nueva distancia: {nueva_distancia}")
            print(f"Comparamos {nueva_distancia} < {distancias[vecino]}")
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                print(f"Se actualiza distancai de {vecino} a {nueva_distancia}")
                heapq.heappush(heap, (nueva_distancia,vecino))
                print(f"Distancias: {distancias}")
            else:
                print(f"No se actualiza, el camino actual es más largo")
    print(f"\nDistancias finales")
    for nodo,distancia in distancias.items():
        print(f"-{nodo}:{distancia}")
    return distancias

