"""#Funciones
def suma(a, b):
    r=a+b
    return r
def resta(a, b):
    r=a-b
    return r
def multi(a, b):
    r=a*b
    return r
def divi(a, b):
    r=a/b
    return r
def i_f(m):
    z=float(input(m))
    return z
    """
#print (divi(12,3))
#print (suma(12,3))
#print (resta(12,3))
#print (multiplicacion(12,3))
from Operaciones import Basicas as ba
x=ba.i_f("Ingrese el primer valor: ")
y=ba.i_f("Ingrese el segundo valor: ")
opc_operacion=input("Operaciones :1.Suma 2.Resta 3.Multiplicacion 4.Division Elegir: ")
match opc_operacion:
    case "1":
        resultado=ba.suma(x,y)
    case "2":
        resultado=ba.resta(x,y)
    case "3":
        resultado=ba.multi(x,y)
    case "4":
        resultado=ba.divi(x,y)
print(f"El resultado de la operacion es: {resultado:.1f}")