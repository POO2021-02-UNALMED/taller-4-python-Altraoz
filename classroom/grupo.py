from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:
    
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista != None):
            lista.append(alumno)
            self.listadoAlumnos = lista
        else:
            self.listadoAlumnos = [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    
    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo
