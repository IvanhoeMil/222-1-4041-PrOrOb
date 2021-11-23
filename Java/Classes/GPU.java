package Java.Classes;
public class GPU {
    public int id;
    public String model;
    public String brand;
    public int memory_size;
    public String cooling_type;

    public GPU(int id, String model, String brand, int memory_size, String cooling_type) {
        this.id = id;
        this.model = model;
        this.brand = brand;
        this.memory_size = memory_size;
        this.cooling_type = cooling_type;
    }
}
