from jugadores import Jugador


class Equipo:
    nombre_equipo = None
    barrio = None
    capitan = None

    def __init__(self):
        listaJugadores = []
        listaHorariosQuePuede = [[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]


    def nombreEquipo(self,nombreEquip):
        self.nombre_equipo = nombreEquip

    def setBarrio(self, nombreBarrio):
        self.barrio = nombreBarrio

    def setJugador(self, jugador):
        self.listaJugadores.append(jugador)

    def setHorario(self, dia, turno):
        self.listaHorariosQuePuede[dia][turno]

    def setCapitan(self, nombreJug):
        for item in self.listaJugadores:
            if item.nombre_Jug == nombreJug:
                self.capitan = item.nombre_Jug

    def HorariosQuePuede(self, dia , turno):
        self.listaHorariosPorDia[dia][turno] = True





