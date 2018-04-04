from personas import Personas


class Familia (object):

    def __init__(self):
        listaPersonas = []

    def agregarPersona(self, nombrePersona):
        unaPers = Personas(nombrePersona)
        self.listaPersonas.append(unaPers)

    def PromedioCaloriasFamilia(self):
        CaloriasTotalesFamilia = 0

        for persona in self.listaPersonas:
            CaloriasTotalesFamilia += persona.CaloriasConsumidas

        PromedioCaloriasFamilia = CaloriasTotalesFamilia / len(self.listaPersonas)

    def MenorPersonaConCalorias(self):
        mayor = 0

        for persona in self.listaPersonas:
            if persona.CaloriasConsumidas > mayor:
                mayor = persona.CaloriasConsumidas

        return mayor

    def MayorPersonaConCalorias(self):
        menor = 1000000

        for persona in self.listaPersonas:
            if persona.CaloriasConsumidas < menor:
                menor = persona.CaloriasConsumidas


        return menor