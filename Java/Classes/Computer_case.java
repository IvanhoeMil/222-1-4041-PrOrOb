package Java.Classes;
public class Computer_case {
    public int id;
    public String brand;
    public String color;
    public String material;
    public String form_Factor;

    public Computer_case(int id, String brand, String color, String material, String form_Factor) {
        this.id = id;
        this.brand = brand;
        this.color = color;
        this.material = material;
        this.form_Factor = form_Factor;
    }

    public String get_case(String brand, String form_Factor) {
        return brand + " " + form_Factor;
    }
    
}
