import datetime
import calendar


class Empleado(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None
    telefono = None

    def init(self):
        lista_horario = [True, True, True, True, True, False, False]
        lista_asistencia = [datetime(2018, 02, 15), datetime(2018, 02, 16), datetime(2018, 02, 19)]

    def porcentajeAsistencia(self, año, mes):

        dias_que_fue = 0
        dia_que_tiene_que_ir = 0
        dia_del_mes = calendar.monthrange(año, mes)[1]

        for item in range(dia_del_mes):

            fecha = datetime.date(año, mes, item)

            if fecha.weekday() >= 0 and fecha.weekday() <= 4:

                if fecha == self.lista_asistencia[dia_que_tiene_que_ir]:
                    dias_que_fue += 1

                dia_que_tiene_que_ir += 1

        promedio_mes = dias_que_fue / dia_del_mes * 100

        return promedio_mes