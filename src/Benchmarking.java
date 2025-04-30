import java.util.Random;

public class Benchmarking {
    private MetodosOrdenamiento metodosOrdenamiento;

    public Benchmarking() {
        metodosOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(100000);

        
        //long inicioMillis = System.currentTimeMillis();
        //long inicioNano = System.nanoTime();
        //System.out.println("Millis: " + inicioMillis);
        //System.out.println("Nano: " + inicioNano);

        
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);

        double tiempoNano = medirConNanoTime(tarea);
        System.out.println("Tiempo con nanoTime " + tiempoNano + " segundos");
        double milisegundos = medirConCurrentTime(tarea);
        System.out.println("Tiempo con currentTime " + milisegundos + " milisegundos");
    }

    private int[] generarArregloAleatorio(int tam) {
        int[] arreglo = new int[tam];
        Random random = new Random();
        for (int i = 0; i < tam; i++) {
            arreglo[i] = random.nextInt(10000); 
        }
        return arreglo;
    }

    public double medirConNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }

    public double medirConCurrentTime(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0;
    }

    public static void main(String[] args) {
        new Benchmarking();
    }
}
