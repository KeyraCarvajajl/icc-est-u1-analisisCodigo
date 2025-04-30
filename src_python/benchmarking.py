import random
import time

from metodos_Ordenamiento import MetodosOrdenamiento

class Benchmarking: 
    
    def __init__(self):
        print('Bench inicializado') 
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
            numero = random.randint(0, 99999)
            array.append(numero)
        return array
    
    
    # import time
    # ejecutar tarea tarea()
    # x = time.time()
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time() 
        tarea()
        fin = time.time()
        return (fin - inicio) / 1000
        
    
    # x = time.time_ns()    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()  
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0