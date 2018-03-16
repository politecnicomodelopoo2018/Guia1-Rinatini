from alumno import Alumnos

a = Alumnos()

a.AgregarMateria("Matematica")
a.AgregarMateria("Laboratorio")
a.AgregarMateria("Lengua")


a.AgregarNota_a_Materia("Matematica",6)
a.AgregarNota_a_Materia("Matematica",4)
a.AgregarNota_a_Materia("Matematica",8)

a.AgregarNota_a_Materia("Laboratorio",7)
a.AgregarNota_a_Materia("Laboratorio",7)
a.AgregarNota_a_Materia("Laboratorio",7)

a.AgregarNota_a_Materia("Lengua",5)
a.AgregarNota_a_Materia("Lengua",5)
a.AgregarNota_a_Materia("Lengua",5)



print(a.PromedioMateria("Matematica"))
print(a.PromedioMateria("Laboratorio"))
print(a.PromedioMateria("Lengua"))

print(a.PromedioGeneral())

