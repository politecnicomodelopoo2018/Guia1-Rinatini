import datetime

from emprresa import Empresa
from emplleado import Empleado


Unaempr = Empresa()
Unemp = Empleado()

Unemp.nombre = 'Pepe'
Unemp.apellido = 'Snow'
Unemp.fecha_nacimiento = datetime.date(1995, 10, 24)
Unemp.telefono = '1234-1234'

Unaempr.agregarEmpleadoALista(Unemp)

Unemp.nombre = 'SoyKhea'
Unemp.apellido = 'Bro'
Unemp.fecha_nacimiento = datetime.date(1995, 11, 25)
Unemp.telefono = '1245-1245'

Unaempr.agregarEmpleadoALista(Unemp)

Unemp.nombre = 'Pito'
Unemp.apellido = 'Caleiro'
Unemp.fecha_nacimiento = datetime.date(1995, 12, 25)
Unemp.telefono = '1256-1256'

Unaempr.agregarEmpleadoALista(Unemp)

Unemp.porcentajeAsistencia(2000, 2)
