from equipos import Equipo


class Torneo:
    def __init__(self):
        listaEquipos = []
        listaPosibPartidos = [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]
        partidosJugados = []


    def setEquipo(self, unEquipo):
        self.listaEquipos.append(unEquipo)

    def setPosiblesHorariosPartidos(self):
        for i in range(7):
            for j in range(3):
                for item in self.listaEquipos:
                    if item.listaHorariosQuePuede[i][j]:
                        self.listaPosibPartidos[i][j].append(item)
        for i in range(7):
            for j in range(3):
                for equi1 in self.listaPosibPartidos[i][j]:
                    for equi2 in self.listaPosibPartidos[i][j]:
                         if equi1==equi2:
                             continue

















