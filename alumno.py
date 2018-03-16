import datetime
from materias import  Materias

class Alumnos(object):

    nombre = None
    apellido = None
    fechaNac = None

    def __init__(self, nombre = None , apellido = None):
        self.listaMaterias = []
    def setNombre(self, nomb):
        self.nombre = nomb
    def setApellido(self, apell):
        self.apellido = apell
    def setFechaNac(self, fecha):
        self.fechaNac = fecha
    def AgregarMateria(self, nombre_mat):
        laMateria = Materias(nombre_mat)
        self.listaMaterias.append(laMateria)
    def AgregarNota_a_Materia(self, nombre_mat, nota):
        for mat in self.listaMaterias:
            if mat.nombre == nombre_mat:
                mat.AgregarNota(nota)
                return True
    def PromedioMateria(self,materia):
        for mat in self.listaMaterias:
            if mat.nombre == materia:
                return mat.PromedioMateria()
    def PromedioGeneral(self):
        s = 0
        for item in self.listaMaterias:
            s += item.PromedioMateria()
        return s/len(self.listaMaterias)

    def MayorPromedio(self):
        mayor_prom = 0
        for item in self.listaMaterias:
            if item.PromedioMateria > mayor_prom:
                mayor_prom = item.PromedioMateria
        return mayor_prom
    def MenorPromedio(self):