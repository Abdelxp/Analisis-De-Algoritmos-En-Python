#Convertir numeros decimales a binarios
"""
13=1101
resto = n % 2 --> 13 % 2 = 1 #digito
cociente = n // 2 --> 13 // 2 = 6
6 % 2 = 0 #digito
6 // 2 = 3
3 % 2 = 1 #digito
3 // 2 = 1
1 % 2 = 1 #digito
1 // 2 = 0  

"""
def decimal_a_binario(n):
    # Caso Base
    print(f"Iniciamos con: {n}")
    if n == 0:
        print("Caso Base: 0")
        return ""
    else:
        # Caso Recursivo
        resto = n % 2
        cociente = n // 2
        print(f"Resto: {resto}, Cociente: {cociente}")
        return decimal_a_binario(cociente) + str(resto)
        # decimal_a_binario(13) +´1´ = [esperando]=(´110') + '1' = '1101'
        # decimal_a_binario(6) +´0´ = [esperando]=('11') + '0'  =´110´
        # decimal_a_binario(3) +´1´ = [esperando]=(´1´) + '1'  = '11'
        # decimal_a_binario(1) +´1´ = [esperando]=(´´) + '1'  = '1'
        # decimal_a_binario(0) = ''  # Caso Base
print(f"De base decimal a binario es: {decimal_a_binario(13)}")