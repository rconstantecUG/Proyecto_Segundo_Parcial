from PySide6.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QDate
from datetime import datetime
from Datos.Estudiante_Dao import EstudianteDao
from Dominio.Estudiante import Estudiante
from GUI.vtn_principal import Ui_Form_Students
import statistics

class EstudianteServicio(QMainWindow):
    def __init__(self):
        # Constructor de la clase EstudianteServicio
        super().__init__()

        # Inicialización de la interfaz de usuario
        self.ui = Ui_Form_Students()
        self.ui.setupUi(self)

        # Creación de una instancia de Estudiante con valores por defecto
        self.estudiante = Estudiante("","","","","","","")

        # Conexión de botones a funciones
        self.ui.pushButtonRegistrar.clicked.connect(self.grabar)
        self.ui.pushButtonPromedio.clicked.connect(self.calculo_promedio)
        self.ui.pushButtonMedia.clicked.connect(self.calculo_media)
        self.ui.pushButtonModa.clicked.connect(self.calculo_moda)
        self.ui.pushButtonMinimo.clicked.connect(self.calculo_minimo)
        self.ui.pushButtonMaximo.clicked.connect(self.calculo_maximo)

        # Obtención de la lista de estudiantes desde el DAO
        self.estudiantes = EstudianteDao.seleccionar_estudiantes()

    def grabar(self):
        # Función para grabar los datos del estudiante
        if self.validar_datos():
            # Obtener y capitalizar los datos ingresados desde la interfaz de usuario
            nombre = self.ui.textEditNombre.toPlainText().capitalize()
            apellido = self.ui.textEditApellido.toPlainText().capitalize()
            cedula = self.ui.textEditCedula.toPlainText().capitalize()
            peso = self.ui.textEditPeso.toPlainText()
            estatura = self.ui.textEditEstatura.toPlainText()
            fecha_nacimiento = self.ui.dateEdit.text()
            edad = self.calcular_edad(fecha_nacimiento)

            # Actualizar las propiedades del objeto estudiante con los datos ingresados
            self.estudiante.nombre = nombre
            self.estudiante.apellido = apellido
            self.estudiante.cedula = cedula
            self.estudiante.peso = peso
            self.estudiante.estatura = estatura
            self.estudiante.fecha_nacimiento = fecha_nacimiento
            self.estudiante.edad = edad

            try:
                # Intentar insertar el estudiante en la base de datos a través del DAO
                EstudianteDao.insertar_estudiante(self.estudiante)

                # Limpiar los campos de la interfaz después de la inserción exitosa
                self.ui.textEditNombre.setText("")
                self.ui.textEditApellido.setText("")
                self.ui.textEditCedula.setText("")
                self.ui.textEditPeso.setText("")
                self.ui.textEditEstatura.setText("")

                # Mostrar un cuadro de información indicando el éxito de la operación
                QMessageBox.information(self, "Título del cuadro de información",
                                        "Estudiante guardado de manera correcta")

            except Exception as e:
                # Manejar excepciones en caso de errores durante la inserción
                print(e)
        else:
            # Mostrar una advertencia si faltan datos o si la entrada es incorrecta
            QMessageBox.warning(self, 'Advertencia', 'Falta ingresar datos o Verifique la entrada de los mismos')

    def validar_datos(self):
        # Función para validar los datos ingresados en la interfaz de usuario
        return (len(self.ui.textEditNombre.toPlainText()) > 0
                and len(self.ui.textEditApellido.toPlainText()) > 0
                and len(self.ui.textEditPeso.toPlainText()) > 0
                and len(self.ui.textEditEstatura.toPlainText()) > 0
                and self.is_numeric(self.ui.textEditPeso.toPlainText())
                and self.is_numeric(self.ui.textEditEstatura.toPlainText())
                and self.validar_fecha(self.ui.dateEdit.text())
                and len(self.ui.textEditCedula.toPlainText()) == 10
                and self.is_numeric(self.ui.textEditCedula.toPlainText())
                )

    def calculo_promedio(self):
        # Función para calcular y mostrar el promedio de peso, estatura y edad de los estudiantes
        peso = self.calcular_promedio(self.estudiantes, 'peso')
        estatura = self.calcular_promedio(self.estudiantes, 'estatura')
        edad = self.calcular_promedio(self.estudiantes, 'edad')
        mensaje = f'Promedio de Peso: {peso:.2f}\n' \
                  f'Promedio de Estatura: {estatura:.2f}\n' \
                  f'Promedio de Edad: {edad:.0f}'

        QMessageBox.information(self, "Promedios", mensaje)

    def calculo_media(self):
        # Función para calcular y mostrar la media de peso, estatura y edad de los estudiantes
        peso = self.calcular_media(self.estudiantes, 'peso')
        estatura = self.calcular_media(self.estudiantes, 'estatura')
        edad = self.calcular_media(self.estudiantes, 'edad')
        mensaje = f'Media de Peso: {peso:.2f}\n' \
                  f'Media de Estatura: {estatura:.2f}\n' \
                  f'Media de Edad: {edad:.0f}'

        QMessageBox.information(self, "Medias", mensaje)

    def calculo_moda(self):
        # Función para calcular y mostrar la moda de peso, estatura y edad de los estudiantes
        peso = self.calcular_moda(self.estudiantes, 'peso')
        estatura = self.calcular_moda(self.estudiantes, 'estatura')
        edad = self.calcular_moda(self.estudiantes, 'edad')
        mensaje = f'Moda de Peso: {peso:.2f}\n' \
                  f'Moda de Estatura: {estatura:.2f}\n' \
                  f'Moda de Edad: {edad:.0f}'

        QMessageBox.information(self, "Moda", mensaje)

    def calculo_minimo(self):
        # Función para calcular y mostrar el valor mínimo de peso, estatura y edad de los estudiantes
        peso = self.calcular_minimo(self.estudiantes, 'peso')
        estatura = self.calcular_minimo(self.estudiantes, 'estatura')
        edad = self.calcular_minimo(self.estudiantes, 'edad')
        mensaje = f'Minimo de Peso: {peso:.2f}\n' \
                  f'Minimo de Estatura: {estatura:.2f}\n' \
                  f'Minimo de Edad: {edad:.0f}'

        QMessageBox.information(self, "Minimo", mensaje)

    def calculo_maximo(self):
        # Función para calcular y mostrar el valor máximo de peso, estatura y edad de los estudiantes
        peso = self.calcular_maximo(self.estudiantes, 'peso')
        estatura = self.calcular_maximo(self.estudiantes, 'estatura')
        edad = self.calcular_maximo(self.estudiantes, 'edad')
        mensaje = f'Maximo de Peso: {peso:.2f}\n' \
                  f'Maximo de Estatura: {estatura:.2f}\n' \
                  f'Maximo de Edad: {edad:.0f}'

        QMessageBox.information(self, "Maximo", mensaje)

    def validar_fecha(self, fecha_ingresada):
        # Función para validar el formato y la validez de una fecha ingresada
        # Obtener la fecha actual
        fecha_actual = datetime.now().date()

        try:
            # Convertir la fecha ingresada a un objeto datetime
            fecha_ingresada = datetime.strptime(fecha_ingresada, "%d/%m/%Y").date()
        except ValueError:
            # Manejar una excepción si el formato de la fecha no es válido
            return False

        # Verificar si la fecha ingresada es mayor que la fecha actual
        if fecha_ingresada > fecha_actual:
            print("Error: La fecha ingresada es mayor que la fecha actual.")
            return False

        return True

    def is_numeric(self, number):
        # Función para verificar si una cadena es numérica
        try:
            # Intenta convertir el texto a un número
            float(number)
            return True
        except ValueError:
            # Si hay una excepción, el texto no es un número
            return False

    def calcular_edad(self, fecha_ingresada):
        # Función para calcular la edad a partir de una fecha de nacimiento
        # Convierte la fecha ingresada en formato de cadena a un objeto QDate
        fecha_nacimiento = QDate.fromString(fecha_ingresada, "yyyy-MM-dd")

        # Obtener la fecha actual
        fecha_actual = QDate.currentDate()

        # Calcular la diferencia en años
        edad = fecha_actual.year() - fecha_nacimiento.year() - (
                (fecha_actual.month(), fecha_actual.day()) < (fecha_nacimiento.month(), fecha_nacimiento.day()))

        # Devolver la edad como cadena
        return str(edad)

    def calcular_promedio(self, estudiantes, atributo):
        # Función para calcular el promedio de un atributo específico en la lista de estudiantes
        valores = [getattr(estudiante, atributo) for estudiante in estudiantes if
                   getattr(estudiante, atributo) is not None]
        promedio = sum(valores) / len(valores) if valores else 0
        return promedio

    def calcular_media(self, estudiantes, atributo):
        # Función para calcular la mediana de un atributo específico en la lista de estudiantes
        valores = [getattr(estudiante, atributo) for estudiante in estudiantes if
                   getattr(estudiante, atributo) is not None]
        media = statistics.median(valores) if valores else 0
        return media

    def calcular_maximo(self, estudiantes, atributo):
        # Función para calcular el valor máximo de un atributo específico en la lista de estudiantes
        valores = [getattr(estudiante, atributo) for estudiante in estudiantes if
                   getattr(estudiante, atributo) is not None]
        maximo = max(valores) if valores else 0
        return maximo

    def calcular_moda(self, estudiantes, atributo):
        # Función para calcular la moda de un atributo específico en la lista de estudiantes
        valores = [getattr(estudiante, atributo) for estudiante in estudiantes if
                   getattr(estudiante, atributo) is not None]
        moda = statistics.mode(valores) if valores else 0
        return moda

    def calcular_minimo(self, estudiantes, atributo):
        # Función para calcular el valor mínimo de un atributo específico en la lista de estudiantes
        valores = [getattr(estudiante, atributo) for estudiante in estudiantes if
                   getattr(estudiante, atributo) is not None]
        minimo = min(valores) if valores else 0
        return minimo
