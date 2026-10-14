lista=[1, 3, 5, 7, 9]
objetivo=7
"""if objetivo in lista:
    print(f"El valor {objetivo} se encuentra en la lista")  
else:
    print(f"El valor {objetivo} no se encuentra en la lista")"""
def buscar(lista,objetivo):
    print(f"lista: {lista}")
    print(f"objetivo buscado: {objetivo}")
    for elemento in lista:#elemento es cada valor de la lista
        print(f"Comparando ({elemento}) con ({objetivo})")
        if elemento==objetivo:
            print(f"Encontrado!")
            return True
    print(f"El valor {objetivo} no se encuentra en la lista")
    return False
if buscar(lista,objetivo):
    print(f"El valor {objetivo} se encuentra en la lista")  
else:
    print(f"El valor {objetivo} no se encuentra en la lista")