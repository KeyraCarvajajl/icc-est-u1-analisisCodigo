#  Ejecutar benchmarking
# import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_Ordenamiento import MetodosOrdenamiento

import matplotlib.pyplot as plt

if __name__== "_main_":
    # Instancias de clases
    benchmark = Benchmarking()
    metodos_ordenamiento = MetodosOrdenamiento()

    tamanios = [500, 1000, 2000]

    metodos = {
        "Burbuja": metodos_ordenamiento.sortByBubble,
        "Seleccion": metodos_ordenamiento.sort_seleccion,
    }

    resultados = []

    for tam in tamanios:
        arreglo = benchmark.build_arreglo(tam)  # ✅ método de instancia
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo[:])  # ✅ corregido
            resultados.append((tam, nombre, tiempo))

    # Mostrar resultados por consola
    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}  Método: {nombre}  Tiempo: {tiempo:.6f} segundos")

    # Organizar resultados por método
    tiempos_by_metodo = {nombre: [] for nombre in metodos.keys()}
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    # Graficar
    plt.figure(figsize=(10, 6))
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre)

    plt.title("Comparativa de Métodos de Ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo Metodos")
    plt.legend()
    plt.grid(True)
    plt.show()