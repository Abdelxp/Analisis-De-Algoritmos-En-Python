#Factores primos
# 6 = 2 x 3,  7 = 7 x 1, 3 = 3 x 1
#Elegir el menor divisor posible desde el 2

def factores_primos (n):
    print(f"Iniciamos con n: {n}")
    i = 2 #Es el menor primo
    factores = []
    while i * i <= n: #4 <= 11
        print(f"Probar divisor i={i}") #2
        if n % i == 0: # 11%2==0 F
            print(f"{i} si es factor primo, Divimos {n} //{i}")
            n//=i # n = n // i  #Dividimos el número
            factores.append(i)
            print(f"Nuevo valor de n: {n}")
        else:
            print(f"{i} no es factor primo, probar con {i+1}") #
            i+=1 # i=i+1 #Probando con el siguiente número
    if n>1:
        factores.append(n)
        print(f"{n} es un primo mayor restante")
    return factores

print(factores_primos(21))