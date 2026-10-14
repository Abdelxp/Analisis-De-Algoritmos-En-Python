#Invertir la cadena de una lista
"""
hola--> aloh
cadena = "algoritmo"
ultimo = cadena[-1] # "o"
resto = cadena[:-1] # "algoritm"

"""
def invertir_cadena(cadena):
    # Caso Base
    print(f"Iniciamos con: {cadena}")
    if len(cadena) == 0:
        print("Caso Base: retornar cadena vacia")
        return ""
    else:
        # Caso Recursivo
        ultimo = cadena[-1] # "o"
        resto = cadena[:-1] # "algoritm"
        print(f"Nos quedamos con el  {ultimo} y enviamos el {resto}")
        return ultimo + invertir_cadena(resto)
        #  'a' + invertir_cadena('hol') = 'a' + [esperando]('hol') = 'a' + 'loh' = 'aloh'
        #  'l' + invertir_cadena('ho') = 'l' + [esperando]('ho') = 'l' + 'oh' = 'loh'
        #  'o' + invertir_cadena('h') = 'o' + [esperando]('h') = 'o' + 'h' = 'oh'
        #  'h' + invertir_cadena('') = 'h' + [esperando]('') = h + "" =  h
print(f"Palabra invertida es: {invertir_cadena('hola')}")