#Algoritmo voraz
"""
Es la desicion mas rapida,aunque no siempre es la mejor.
Elige lo mejor que tiene en el momento ,sin pensar mucho en el futuro.

Propiedades nesesarias del problema:
1.Subestructura optima
2.Elección voraz

"""
 
def cambio_monedas(monedas,cantidad):
    print(f"Cantidad a cambiar: {monedas}")
    print(f"Monedas disponibles: {cantidad}")
    monedas.sort(reverse=True)#50,20,10,5,1
    print(f"Monedas disponibles (mayor a menor): {monedas}")
    resultado=[]
    for moneda in monedas:
        print(f"Probando con la moneda: {monedas}")
        while cantidad >= moneda:
            cantidad-=moneda
            resultado.append(moneda)
            print(f"Agregamos {moneda}. Cantidad restante: {cantidad}")
    return resultado        

monedas=[1,20,10,5,50]
cantidad=int(input("Ingrese la cantidad a cambiar:  "))
result = (cambio_monedas(monedas,cantidad))
mon_50 = result.count(50)
mon_20 = result.count(20)
mon_10 = result.count(10)
mon_5 = result.count(5)
mon_1 = result.count(1)
print(f"""
╔════════════════════════════╗
║         RESULTADOS:        ║
╠════════════════════════════╣
║ Billetes de 50: {mon_50}   ║
║ Billetes de 20: {mon_20}   ║
║ Billetes de 10: {mon_10}   ║
║ Monedas de 5: {mon_5}      ║
║ Monedas de 1: {mon_1}      ║
╚════════════════════════════╝

""")