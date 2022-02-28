#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# - Color
# - Ruedas
# - Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# - Velocidad
# - Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:

    def color(self):
        self.colorrojo=True
        print('El color es rojo')

    def ruedas(self):
        self.ruedasinvierno=True

    def puertas(self):
        self.cincopuertas=True

class Coche(Vehiculo):
    def velocidad(self):
        self.granvelocidad=True
    def cilindrada(self):
        self.amga45S=True

p = Coche() #objeto(instancia) de clase
print(dir(p))



