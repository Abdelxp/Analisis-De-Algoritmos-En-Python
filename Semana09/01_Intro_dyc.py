#Divide y conquista
"""
Estrategia de diseños de algoritmos
1. Dividir el problema en subproblemas
2. Conquista resolviendo los subproblemas
3. Combinar las soluciones de los subproblemas
--------------------
Maximo común divisor (MCD)
8 - 12 | 2
4 - 6 | 2
2 - 3
MCD(8,12) = 4
--->Algoritmo de Auclides
MCD(a, b) = MCD(b, a%b)
1. Divide: MCD(a, b) ---> MCD(b, a%b)
2. Conquista: MCD(a, b) ---> MCD(b, a%b)
3. Combina: retornar los resultados

"""
def mcd(a, b):
    print(f"Trabajamos con {a} y {b}")
    if b == 0:
        print(f"b=0, MCD es {a}")
        return a
    else:
        resto = a % b
        print(f"{a}%{b}={resto}... Llamamos al MCD({b},{resto})")
        return mcd(b, resto)
r=mcd(8,12)
print(f"El mcd es: {r}")



