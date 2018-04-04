import datetime
from datos import  Datos

class Persona(object):
    nombre = None

    def __init__(self,nombrePer):
        self.nombre = nombrePer
        listaDatos = []

    def agregarDatos(self, _fecha, _peso, _altura):
        unDato = Datos()
        unDato.setPesoEnFecha(_peso, _altura, _fecha)
        self.listaDatos.append(unDato)

    def verDatosEnFecha(self,fecha):
        for item in self.listaDatos:
            if item.fecha == fecha:
                return item.peso, item.altura

    def PromedioPesoYAlturaEnAño(self, año):
        sumaPeso = 0
        sumaAltura = 0
        cantidadDeMedias = 0

        for item in self.listaDatos:
            if item.fecha.year() == año:
                sumaPeso += item.peso
                sumaAltura += item.altura
                cantidadDeMedias += 1

        promedioPeso = sumaPeso / cantidadDeMedias
        promedioAltura = sumaAltura / cantidadDeMedias

        return  promedioAltura, promedioPeso

    def PorcentajeCrecimiento(self, año):
        for item in self.listaDatos:
            if item.fecha.year() == año:
                altura1 = item.altura
                break

        for item2 in self.listaDatos:
            if item2.fecha.year() == año + 1:
                altura2 = item2.altura
                break

        porcentajeCrecimiento = altura1 * 100 / altura2