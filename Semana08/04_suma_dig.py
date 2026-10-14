#   Suma digitos
"""
5738
resto = n % 10 --> 5738 % 10 = 8 #digito
cociente = n // 10 --> 5738 // 10 = 573
---
resto = n % 10 --> 573 % 10 = 3 #digito
cociente = n // 10 --> 573 // 10 = 577
---
resto = n % 10 --> 57 % 10 = 7 #digito
cociente = n // 10 --> 57 // 10 = 5 #digito
---> 5 + 7 + 3 + 8 = 23

"""
def suma_digitos(n):
    # Caso Base
    print(f"Iniciamos con {n}")
    if n < 10:
        print(f"Caso Base: retornamos {n}")
        return n
    else:
        # Caso Recursivo
        resto = n % 10
        cociente = n // 10
        print(f"Enviando {cociente}, quedando con  {resto}")
        return n % 10 + suma_digitos(n // 10)
        #  8 + suma_digitos(573) -> 8 + 15 =23
        #  3 + suma_digitos(57) -> 3 + 12 =15
        #  7 + suma_digitos(5) -> 7 + 5 =12 
        #  5 + suma_digitos(0) -> 5 + 0 =5
print(f"La suma de los digitos es: {suma_digitos(5738)}")