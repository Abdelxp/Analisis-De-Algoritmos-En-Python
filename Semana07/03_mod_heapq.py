#Modulo heapq
"""
Implementar colas con prioridad
heapppush: agregar un elemento a la lista priorizada
heappop: sacar o mostrar el elemento prioritario 

"""
import heapq
heap = []
print(f"Lista heapq :{heap}")
#Priorizar segun el valor del push
heapq.heappush(heap,(54,'B'))
heapq.heappush(heap,(25,'C'))
heapq.heappush(heap,(12,'D'))
heapq.heappush(heap,(34,'A'))
print(f"Lista heapq priorizada: {heap}")
menor = heapq.heappop(heap)
print(f"Elemento prioritario: {menor}")