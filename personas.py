from platos import Platos

class Personas(object):
    nombre = None
    fecha_Nacimiento = None

    def __init__(self, nomb, fecha):
        self.nombre = nomb
        self.fecha_Nacimiento = fecha

        PlatosComidos = []

    def agregarPlatoAPersona(self, nomPlato):
        unPlato = Platos(nomPlato)

        self.PlatosComidos.append(unPlato)

    def CaloriasConsumidas(self):
        sumaCalorias = 0

        for item in self.PlatosComidos:
            sumaCalorias += item.calorias

        return sumaCalorias



