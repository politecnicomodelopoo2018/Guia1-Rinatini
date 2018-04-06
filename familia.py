from personas import Personas


class Familia (object):

    def __init__(self):
        self.listaPersonas = []

    def agregarPersona(self, UnaPersona):
        self.listaPersonas.append(UnaPersona)

    def PromedioCaloriasFamilia(self):
        CaloriasTotalesFamilia = 0

        for persona in self.listaPersonas:
            CaloriasTotalesFamilia += persona.CaloriasConsumidas()

        PromedioCaloriasFamilia = CaloriasTotalesFamilia / len(self.listaPersonas)

        return PromedioCaloriasFamilia

    def MayorPersonaConCalorias(self):
        mayor = 0

        for persona in self.listaPersonas:
            if persona.CaloriasConsumidas() > mayor:
                mayor = persona.CaloriasConsumidas()
                nombrePersonaMasGorda = persona.nombre

        return nombrePersonaMasGorda

    def MenorPersonaConCalorias(self):
        menor = 10000

        for persona in self.listaPersonas:
            if persona.CaloriasConsumidas() < menor:
                menor = persona.CaloriasConsumidas()
                nombrePersona = persona.nombre

        return nombrePersona
