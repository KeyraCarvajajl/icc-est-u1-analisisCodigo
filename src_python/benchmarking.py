import random
import time

from metodos_Ordenamiento import MetodosOrdenamiento

class Benchmarking: 
    
    def __init__(self):
        print('Bench inicializado') 
        
    def ejemplo(self):
        self.mOrdenamiento = MetodosOrdenamiento()
        
        arreglo = self.build_arreglo(1000)
        
        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMillis = self.contar_con_current_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)
        
        print(f'El tiempo en milisegundos es: {tiempoMillis}')
        print(f'El tiempo en nanosegundos es: {tiempoNano}')
        
        
    def build_arreglo(self, size):
        array = []  
        for i in range(size):
            numero = random.randint(0, 50000)
            array.append(numero)
        return array
    
    
    # import time
    # ejecutar tarea tarea()
    # x = time.time()
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time() 
        tarea()
        fin = time.time()
        return (fin - inicio) / 10000
        
    
    # x = time.time_ns()    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()  
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0
    
    def medir_tiempo(self, tarea, array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio

    def _init_(self):
        print('Bench inicializado')

    def build_arreglo(size):
        return [random.randint(0, 99999) for _ in range(size)]

    def contar_con_current_time_millis(tarea, array):
        inicio = time.time()  
        tarea(array)
        fin = time.time()
        return (fin - inicio) * 1000 

    def contar_con_nano_time(tarea, array):
        inicio = time.perf_counter_ns()
        tarea(array)
        fin = time.perf_counter_ns()
        return fin - inicio  


    def medir_tiempo(tarea, array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio  

    def ejemplo(self):
        mOrdenamiento = MetodosOrdenamiento()
        arreglo = self.build_arreglo(50000)

        arreglo_bubble = arreglo[:]
        arreglo_seleccion = arreglo[:]

        tiempoMillis = self.contar_con_current_time_millis(mOrdenamiento.sortByBubble, arreglo_bubble)
        tiempoNano = self.contar_con_nano_time(mOrdenamiento.sort_seleccion, arreglo_seleccion)

        print(f'Tiempo en milisegundos (Burbuja): {tiempoMillis:.3f} ms')
        print(f'Tiempo en nanosegundos (Selección): {tiempoNano} ns')