import datetime

import calendar

class Empleado(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None
    telefono = None

    def __init__(self):
        lista_horario = [True, True, True, True, True, False, False]
        lista_asistencia = [datetime.date(2018, 2, 15), datetime.date(2018, 2, 16), datetime.date(2018, 2, 19)]

    def porcentajeAsistencia(self, anio, mes):

        dias_que_fue = 0
        dia_que_tiene_que_ir = 0
        dia_del_mes = calendar.monthrange(anio, mes)[1]

        for item in range(dia_del_mes):
            fecha = datetime.date(anio, mes, item)

            if self.lista_horario[fecha.weekday()]:

                for item in self.lista_asistencia:

                    #if fecha == self.lista_asistencia[dia_que_tiene_que_ir]:
                    if fecha == item:
                        dias_que_fue += 1
                        break
                dia_que_tiene_que_ir += 1

        promedio_mes = dias_que_fue / dia_del_mes * 100

        return promedio_mes