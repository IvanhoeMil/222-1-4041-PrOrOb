package Java.Classes;
public class Processor {
    public int id;
    public String brand;
    public String model;
    public int cores;
    public int clockSpeed;

    public Processor(int id, String brand, String model, int cores, int clockSpeed) {
        this.id = id;
        this.brand = brand;
        this.model = model;
        this.cores = cores;
        this.clockSpeed = clockSpeed;
    }
}
