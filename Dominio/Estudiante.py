class Estudiante:
    """
        Clase que represnta a un Estudiante.
    """
    def __init__(self, nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad):
        # Constructor que inicializa las propiedades del estudiante
        self.nombre = nombre  # Nombre del estudiante
        self.apellido = apellido  # Apellido del estudiante
        self.cedula = cedula  # Número de cédula del estudiante
        self.estatura = estatura  # Estatura del estudiante
        self.peso = peso  # Peso del estudiante
        self.fecha_nacimiento = fecha_nacimiento  # Fecha de nacimiento del estudiante
        self.edad = edad  # Edad del estudiante