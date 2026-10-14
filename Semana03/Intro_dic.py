#Diccionarios clave:valor
persona = {"nombre":"Ana", "edad":30, "ciudad":"Arequipa" ,"ciudad2":"Lima"}
print(persona["nombre"])
#print(persona["correo"]) #esto genera un error porque no existe la clave correo
print(persona.get("correo","Error,clave no encontrada")) #esto no genera error, pero devuelve el mensaje de error
persona["correo"]="correo@correo.com"#  Añadir un nuevo clave:valor
print(persona)
print(persona.get("correo","Error,clave no encontrada")) #esto no genera error, pero devuelve el mensaje de error
print("-"*50)
#Mostrar valores del diccionario
for clave in persona:
    print(clave,"-->",persona[clave])
del persona["ciudad2"] #eliminar un elemento del diccionario
print("-"*50)
for clave in persona:
    print(clave,"-->",persona[clave])
"""persona.clear() #eliminar todos los elementos del diccionario 
for clave in persona:
    print(clave,"-->",persona[clave])"""
opc=int(input("Opciones: 1.Limpiar,2:Cancelar, Elegir opcion: "))
match opc:
    case 1:
        persona.clear() #eliminar todos los elementos del diccionario
    case 2:
        print("Proceso cancelado")
print("-"*50)
for clave in persona:
    print(clave,"-->",persona[clave])