import matplotlib
import matplotlib.pyplot as plt
print(matplotlib.__version__)

# Crear una grafica

x = [ 1, 2, 3, 4, 5]
y = [ 2, 4, 6, 8, 10]
nombre_linea = "Linea 1"
plt.plot(x, y,label = nombre_linea, color = "blue")

# Agregar parametros a la grafica
plt.title("Primer grafico")
plt.xlabel("Datos eje X")
plt.ylabel("Datos eje Y")
plt.legend()
plt.show()