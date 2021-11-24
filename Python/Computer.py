""" Computer Elements """

class Case:
    def __init__(self, id, brand, color, material, form_factor):
        self.id = id
        self.brand = brand
        self.color = color
        self.material = material
        self.form_factor = form_factor

    def assemble(self):
        print("Case -> assemble")



class Motherboard:
    def __init__(self, id, brand, model, memory_type, graphics_card_slots, form_factor, max_ram):
        self.id = id
        self.brand = brand
        self.model = model
        self.memory_type = memory_type
        self.graphics_card_slots = graphics_card_slots
        self.form_factor = form_factor
        self.max_ram = max_ram

    def assemble(self):
        print("Motherboard -> assemble")



class Memory:
    def __init__(self, id, brand, model, memory_type, memory_size):
        self.id = id
        self.brand = brand
        self.model = model
        self.memory_type = memory_type
        self.memory_size = memory_size

    def handle_tasks(self):
        print("Memory -> handle_tasks")



class Processor:
    def __init__(self, id, brand, model, cores, speed):
        self.id = id
        self.brand = brand
        self.model = model
        self.cores = cores
        self.speed = speed
    
    def process(self):
        print("Processor -> process")


class GPU:
    def __init__(self, id, brand, model, memory_size, cooling_type):
        self.id = id
        self.brand = brand
        self.model = model
        self.memory_size = memory_size
        self.cooling_type = cooling_type

    def render(self):
        print("GPU -> render")



class Data_Storage_Device:
    def __init__(self, id, brand, model, memory_size, type):
        self.id = id
        self.brand = brand
        self.model = model
        self.memory_size = memory_size
        self.type = type

    def store(self):
        print("Data_Storage_Device -> store")



class Keyboard:

    def __init__(self, id, brand, model, size, color):
        self.id = id
        self.brand = brand
        self.model = model
        self.size = size
        self.color = color
    
    def typing(self):
        print("Keyboard -> typing")



class Monitor:

    def __init__(self, id, brand, size, resolution, refresh_rate, video_inputs):
        self.id = id
        self.brand = brand
        self.size = size
        self.resolution = resolution 
        self.refresh_rate = refresh_rate
        self.video_inputs = video_inputs

    def display(self):
        print("Monitor -> display")




class Computer:

    def __init__(self, case, motherboard, memory, processor, gpu, data_storage_device, keyboard, monitor):
        self.case = case
        self.motherboard = motherboard
        self.memory = memory
        self.processor = processor
        self.gpu = gpu
        self.data_storage_device = data_storage_device
        self.keyboard = keyboard
        self.monitor = monitor

    def boot(self):
        print("Computer -> boot")


new_computer = Computer(Case(1, "Asus", "Black", "Plastic", "ATX"), Motherboard(1, "Asus", "Z370", "DDR4", 4, "ATX", 16), Memory(1, "Kingston", "HyperX", "DDR4", 16), Processor(1, "Intel", "i7-7700HQ", 4, 3.5), GPU(1, "Nvidia", "GTX1050", "2GB", "Fan"), Data_Storage_Device(1, "Kingston", "HyperX", "1TB", "SSD"), Keyboard(1, "Logitech", "K120", "Medium", "Black"), Monitor(1, "Samsung", "27 Inch", "1920x1080", 120, "HDMI"))

"""print(new_computer.case.brand)"""

new_computer.boot()
new_computer.case.assemble()
new_computer.motherboard.assemble()
new_computer.memory.handle_tasks()
new_computer.processor.process()
new_computer.gpu.render()
new_computer.data_storage_device.store()
new_computer.keyboard.typing()
new_computer.monitor.display()
