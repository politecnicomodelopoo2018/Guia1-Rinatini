class Materias (object):

    def __init__(self, nombre_mat = None):
        self.listaNotas = []
        self.nombre = nombre_mat
    def AgregarNota(self,nota):
        self.listaNotas.append(nota)
        return True
    def MenorNota(self):
        return  min(self.listaNotas)
    def MayorNota(self):
        return  max(self.listaNotas)
    def PromedioMateria(self):
        if len(self.listaNotas) == 0:
            return False
        promedio = sum(self.listaNotas) / len(self.listaNotas)
        return promedio

