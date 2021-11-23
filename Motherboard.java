public class Motherboard {
    public int id;
    public String model;
    public String brand;
    public String memory_type;
    public String graphics_card_slots;
    public String memory_slots;
    public String form_factor;

    public Motherboard(int id, String model, String brand, String memory_type, String graphics_card_slots, String memory_slots, String form_factor) {
        this.id = id;
        this.model = model;
        this.brand = brand;
        this.memory_type = memory_type;
        this.graphics_card_slots = graphics_card_slots;
        this.memory_slots = memory_slots;
        this.form_factor = form_factor;
    }
}

