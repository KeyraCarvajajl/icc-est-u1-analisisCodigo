
class MetodosOrdenamiento:
    
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo) 
        
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    # arreglo[i], arreglo[j] = arreglo[j], arreglo[i] 
                    aux = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = aux
        return arreglo
    
    def sort_selection(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j
                    
                    aux = arreglo[i]
                    arreglo[i] = arreglo[min_index]
                    arreglo[min_index] = aux
        return arreglo
    
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    # Intercambio correcto
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo

    def sort_seleccion(self, array):
        array = array.copy()
        n = len(array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array

                    
                    