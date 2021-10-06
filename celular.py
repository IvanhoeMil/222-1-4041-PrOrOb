class Celular:
    numero = "3311308954"
    marca = "iPhone"
    compania = "Telcel"

    def mostrar_numero(self, numero):
        print("El numero de celular es "+ numero)

    def mostrar_marca(self, marca):
        print("La marca del celular es: "+marca)

    def mostrar_datos(self, numero, marca, compania):
        print("El celular es un "+marca+" con numero "+numero+ " y compania "+compania )


celular_ivan = Celular()
celular_ivan.mostrar_datos(celular_ivan.numero, celular_ivan.marca,celular_ivan.compania)

celular_naye = Celular()
celular_naye.mostrar_marca("Xiaomi")