#Factorial de un numero
"""
2!=2*1
3!=3*2*1
4!=4*3*2*1
5!=5*4*3*2*1
n!=n*(n-1)*((n-1)-1)*...*1

"""
def factorial(n):#5
    print(f"Iniciamos con  n:{n}")
    if n == 0 or n == 1:
        print("Caso Base: retornar 1")
        return 1
    else:   
        print(f"Caso Recursivo y enviamos factorial({n-1})")
        return n * factorial(n - 1)
        #  5*factorial(4) ->5*24=120
        #  4*factorial(3) -> 4*6=24
        #  3*factorial(2) -> 3*2=6
        #  2*factorial(1) -> 2*1=2
print(f"El factorial es: {factorial(5)}")