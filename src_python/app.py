#  Ejecutar benchmarking
# import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_Ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print("Funciona")
    
    Benchmarking()
    
    benchmark = Benchmarking()
    metodos = MetodosOrdenamiento()
    tamaño = 10000
    arreglo_base = benchmark.build_arreglo(tamaño)
    
    metodos = {
        "Burbuja": metodos.sortByBubble,
        "Seleccion": metodos.sort_selection,
    }
    
    resultados = []
    
    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaResultado = (tamaño, nombre, tiempo)
        resultados.append(tuplaResultado)
        
    for resultado in resultados:
        tamaño, nombre, tiempo = resultado 
        print(f"Tamaño: {tamaño}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")