package Java;
import Java.Classes.*;

public class Main {

    public static void main(String[] args) {

        Computer_case computer_case = new Computer_case(1, "Cooler Master", "Black", "Plastic", "ATX");
        Motherboard motherboard = new Motherboard(1, "Z370", "Asus", "DDR4", 4, 16, "ATX");
        Memory memory = new Memory(1, "Kingston", "DDR4", "HyperX", 16);
        Processor processor = new Processor(1, "Intel", "i7-7700HQ", 4, 3);
        GPU graphics_card = new GPU(1, "Nvidia", "GeForce GTX 1080ti", 8, "Fan");
        Data_Storage data_storage = new Data_Storage(1, "Seagate", "A4X", "1TB", "SSD");
        Keyboard keyboard = new Keyboard(1, "Logitech", "G502", "USB", "Standard");
        Monitor monitor = new Monitor(1, "27 Inch", "1920x1080", "LED", 120, "HDMI");

        Computer new_computer = new Computer(1, computer_case.brand+" "+computer_case.form_Factor, motherboard.brand+" "+motherboard.form_factor, 
        processor.brand+" "+processor.model, memory.brand+" "+memory.memory_size, graphics_card.brand+" "+graphics_card.model,
        data_storage.brand+" "+data_storage.memory_size, keyboard.brand+" "+keyboard.model, monitor.brand+" "+monitor.size);


        System.out.println(new_computer);
    }

}