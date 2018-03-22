from empresa import Empresa


Unaempr = Empresa()
Unemp = Empleado()
Unemp.nombre = 'Pepe'
Unemp.apellido = 'Snow'
Unemp.fecha_nacimiento = datetime(1995,10,24)
Unemp.telefono = '1234-1234'

Unaempr.agregarEmpleadoALista(Unemp)