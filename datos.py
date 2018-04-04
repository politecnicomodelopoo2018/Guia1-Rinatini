class Datos(object):
    fecha = None
    peso = None
    altura = None

    def setPesoEnFecha(self,peso_, altura_, fecha_):
        self.fecha = fecha_
        self.altura = altura_
        self.peso = peso_