import sys
import random 
import time 
from tabulate import tabulate

sys.path.append('../')
from controller.tda.linked.linkedList import LinkedList

if __name__ == "__main__":
    
    lista = LinkedList()
        

    for i in range(25000):
        lista.add(random.randint(0, 25000))
    print(f"Lista orginal: {lista}")


    lista_ordenada = lista.quick_numbers(1)
    
    random_number = random.choice(lista_ordenada.toArray)

    print(f"Lista ordenada: {lista_ordenada}\n")

    print(f"\n\nNúmero aleatorio de la lista: {random_number}")
    
    start_time = time.time()
    valor_encontrados_lineal = lista_ordenada.busqueda_secuencial_lineal(random_number)
    end_time = time.time()
    print(f"\n\nValores encontrados(BUSQUEDA LINEAL) : {valor_encontrados_lineal}")

    start_time2 = time.time()
    valores_encontrados_busqueda_lineal = lista_ordenada.busqueda_lineal_binaria_numeric(random_number)
    end_time2 = time.time()
    print(f"\n\nValores encontrados(BUSQUEDA LINEAL BINARIA): {valores_encontrados_busqueda_lineal}")


    time_data = [
        ["BUSQUEDA LINEAL O SECUENCIAL", (end_time - start_time) * 1000, valor_encontrados_lineal._length],
        ["BUSQUEDA LINEAL BINARIA", (end_time2 - start_time2) * 1000, valores_encontrados_busqueda_lineal._length],
    ]

    table_headers = ["Algoritmo", "Tiempo de ejecución (ms)", "nro. elementos"]
    print("\n")
    print(tabulate(time_data, headers=table_headers, tablefmt="pretty"))
    
    