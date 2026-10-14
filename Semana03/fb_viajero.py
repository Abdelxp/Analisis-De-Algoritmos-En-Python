from itertools import permutations
ciudad=[0,1,2,]
distancias=[[0, 10, 10],
            [10, 0, 20],
            [15, 20, 0]
]
def calcular_distancia(ruta,distancias):
    print(f"--->Calculando distancia para la ruta {ruta}")
    total=0
    for i in range(len(ruta)-1):
        tramo=distancias[ruta[i]][ruta[i+1]]
        total+=tramo
        print(f"Distancia {ruta[i]} a {ruta[i+1]}: {tramo}")
        #volver al inicio
    regreso=distancias[ruta[-1]][ruta[0]]
    #ruta[-1] es el ultimo elemento de la ruta
    print(f"Distancia {ruta[-1]} a {ruta[0]}: {regreso}")
    total+=regreso
    print(f"Distancia total para la ruta es : {total}")
    return total

def mejor_ruta(ciudad,distancias):
    rutas=permutations(ciudad)
    mejor=None
    menor_distancia=float("inf")
    for ruta in rutas:
        d=calcular_distancia(ruta,distancias)
        print(F"Distancia calculada:", {d})
        if d<menor_distancia:
            menor_distancia=d
            mejor=ruta
        else:
            print(f"Ruta {ruta} descartada (distancia {d})")
    return mejor,menor_distancia

ruta,costo=mejor_ruta(ciudad,distancias)
print(f"\n La mejor ruta es {ruta} con un costo de {costo}")