#Moda de un vector
"""
Elemento que mas se repita
vector=["a",3,3,2,"a",4,3,2,"a","a"]
conteo={"a":4,3:3,2:2,4:1}
moda=max(conteo,key=conteo.get)

"""

def moda(vector):
    print(f"Vector de entrada: {vector}")
    conteo={}
    for num in vector:
        if not num in conteo:
            conteo[num]=1
            print(f"No existe, se inicia con 1 conteo [{num}]")
        else:
            conteo[num]+=1
            print(f"Como ya existe, se añade 1 al conteo [{num}]")
        print(f"Conteo actual: {conteo}")
    # noinspection bad-argument-type
    moda=max(conteo,key=conteo.get)
    print(f"La moda encontrada: {moda}")
    print(f"La frecuencia de la moda es: {conteo[moda]}")
    return moda

vector=["a",3,3,2,"a",4,3,2,"a","a"]
moda(vector)



