
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
    
    

                    
                    