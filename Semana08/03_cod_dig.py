#Contar digitos de un número entero
"""
Numero positivo: 789
789//10=78  ...1 digito
78//10=7  ...1 digito
7//10=0  ...1 digito

"""
def contar_digitos(n):
    # Caso Base
    print(f"Iniciamos con {n}")
    if n <10:
        print("Caso Base: retornar 1")
        return 1
    else:
        # Caso Recursivo
        return 1 + contar_digitos(n // 10)
        #  1 + contar_digitos(789//10) -> 1 + 2 =3
        #  1 + contar_digitos(78//10) -> 1 + 1 =2
        #  1 + contar_digitos(7//10) -> 1 + 0 =1
print(f"El numero de digitos es: {contar_digitos(789)}")
