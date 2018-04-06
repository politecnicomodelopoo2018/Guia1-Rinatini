from personas import Personas
from platos import Platos
from familia import Familia
import datetime

laFamilia = Familia()


Fideos = Platos('Fideos',10)
Bife = Platos('Bife',200)
Salchicha = Platos('Salchicha',90)
BarritaCereal = Platos('Barrita de Cereal',3)

laPersona = Personas('Dario', datetime.date(2017, 1, 1))
laPersona.agregarPlatoAPersona(Fideos)
laPersona.agregarPlatoAPersona(Bife)
laPersona.agregarPlatoAPersona(Salchicha)
laPersona.agregarPlatoAPersona(Fideos)
laPersona.agregarPlatoAPersona(BarritaCereal)
laFamilia.agregarPersona(laPersona)


persona1Cals = laPersona.CaloriasConsumidas()

print(persona1Cals)

laPersona = Personas('Manueh', datetime.date(2017, 12,9))
laPersona.agregarPlatoAPersona(Bife)
laPersona.agregarPlatoAPersona(Bife)
laPersona.agregarPlatoAPersona(Salchicha)
laPersona.agregarPlatoAPersona(BarritaCereal)
laPersona.agregarPlatoAPersona(BarritaCereal)
laFamilia.agregarPersona(laPersona)


persona2Calos = laPersona.CaloriasConsumidas()

print(persona2Calos)

promedioFamiliaCals = laFamilia.PromedioCaloriasFamilia()

print(promedioFamiliaCals)

PersonaConMasCalorias = laFamilia.MayorPersonaConCalorias()
PersonaConMenosCalorias = laFamilia.MenorPersonaConCalorias()

print(PersonaConMasCalorias)
print(PersonaConMenosCalorias)

