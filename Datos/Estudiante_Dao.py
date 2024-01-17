from Datos.Conexion import Conexion
from Dominio.Estudiante import Estudiante

class EstudianteDao:
    """
    Clase que encapsula operaciones de acceso a datos para la entidad Estudiante.
    """
    _INSERTAR_ESTUDIANTE = (
        "INSERT INTO ESTUDIANTE (NOMBRE, APELLIDO, CEDULA, ESTATURA, PESO, FECHA_NACIMIENTO, EDAD) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)"
    )

    _SELECCIONAR_ESTUDIANTES = '''
                                SELECT
                                    NOMBRE,
                                    APELLIDO,
                                    CEDULA,
                                    ESTATURA,
                                    PESO,
                                    FECHA_NACIMIENTO,
                                    DATEDIFF(YEAR, fecha_nacimiento, GETDATE()) AS edad
                                FROM
                                    ESTUDIANTE;
                                    '''

    @classmethod
    def insertar_estudiante(cls, estudiante):
        """
        Inserta un nuevo estudiante en la base de datos.
        :param estudiante: Objeto de la clase Estudiante con los datos a insertar.
        """
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    estudiante.nombre,
                    estudiante.apellido,
                    estudiante.cedula,
                    estudiante.estatura,
                    estudiante.peso,
                    estudiante.fecha_nacimiento,
                    estudiante.edad
                )
                cursor.execute(cls._INSERTAR_ESTUDIANTE, datos)
        except Exception as e:
            print(e)

    @classmethod
    def seleccionar_estudiantes(cls):
        """
        Selecciona todos los estudiantes almacenados en la base de datos.
        :return: Lista de objetos de la clase Estudiante.
        """
        try:
            estudiantes = list()
            with Conexion.obtenerCursor() as cursor:
                registros = cursor.execute(cls._SELECCIONAR_ESTUDIANTES).fetchall()
                for registro in registros:
                    estudiante = Estudiante(
                        nombre=registro[0],
                        apellido=registro[1],
                        cedula=registro[2],
                        estatura=registro[3],
                        peso=registro[4],
                        fecha_nacimiento=registro[5],
                        edad=registro[6]
                    )
                    estudiantes.append(estudiante)
            return estudiantes
        except Exception as e:
            print(e)
            return None
