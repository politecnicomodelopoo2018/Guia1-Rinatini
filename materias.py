class Materias (object)

    def __init__(self, nombre_mat = None):
        self.listaNotas = []
    def AgregarNota(self,nota):
        self.listaNotas.append(nota)
        return True
