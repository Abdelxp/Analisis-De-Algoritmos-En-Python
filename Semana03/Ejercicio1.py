#Encontrar un par de numeros que sumen un valor objetivo
numeros=[3,7,11,15,1,8,9,0]
objetivo=10
def encontrar_pareja_suma(lista,objetivo):
    n= len(lista)
    print("Cantidad de elementos en la lista:",n)
    for i in range(n):
        for j in range(i+1,n):
            print(f"Sumando({lista[i]}) + ({lista[j]}) comparando con ({objetivo})")
            if lista[i]+lista[j]==objetivo:
                print(f"Se encontró una pareja: ({lista[i]}) + ({lista[j]}) = ({objetivo})")
                return(lista[i],lista[j])
    print(f"Suma par no encontrado {objetivo}")
    return False


resultado=encontrar_pareja_suma(numeros,objetivo)
if resultado:  
    print(f"Pareja encontrada {resultado}")
else:
    print(f"Pareja no encontrada")