import datetime
from materias import  Materias

class alumnos(object):

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
        for mat in self.listaMaterias
            if mat.nombre == nombre_mat
                mat.AgregarNota(nota)
                return True
    def NotaMayor(self):
        return max(self.listaNotas)
    def NotaMenor(self):
        return min(self.listaNotas)
    def PromedioNota(self):
        promedio = sum(self.listaNotas) / len(self.listaNotas)
        return promedio


a = alumnos(nombre = 'pepe', apellido = 'perez')

n = input("Ingrese nombre: ")
a.setNombre(n)
n = input("Ingrese apellido: ")
a.setApellido(n)

n = int(input("Ingrese año: "))
b = int(input("Ingrese mes: "))
c = int(input("Ingrese dia: "))

fNac = datetime.date(n, b, c)
print(fNac)

a.setFechaNac(fNac)

n = int(input("Ingrese nota 1: "))
b = int(input("Ingrese nota 2: "))
c = int(input("Ingrese nota 3: "))

a.setAgregarNota(n)
a.setAgregarNota(b)
a.setAgregarNota(c)

print(a.NotaMayor())
print(a.NotaMenor())
print(a.PromedioNota())