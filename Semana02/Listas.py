#Datos Estructurados
#Listas
numeros = [1, 2, 3, 4, 5]
print(numeros[3])
#añadir un nuevo elemento
numeros.append(8)
print(numeros)
numeros.insert(1, 5)
print(numeros)
#modificar un valor de la lista
numeros[4]=1
print(numeros)
#Mostrar valores de la lista
for i in range(len(numeros)):
    print(numeros[i])   
#lista de valores
lista_num="" 
for num in numeros:
    lista_num+=str(num)+ " "
print(lista_num)
#Busqueda Basica
var= int(input("Ingrese el valor a buscar: ")) 
if var in numeros:
    print(f"El valor {var} se encuentra en la lista")
else:
    print(f"El valor {var} no se encuentra en la lista")
numeros.remove(1)
print(numeros)
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
print(sum(numeros))