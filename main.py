import sys
from PySide6.QtWidgets import QApplication
from Servicio.estudiante_principal import EstudianteServicio

if __name__ == "__main__":
    # Crear una instancia de la aplicación Qt
    app = QApplication([])

    # Crear una instancia de la ventana principal del servicio de estudiantes
    window = EstudianteServicio()

    # Mostrar la ventana
    window.show()

    # Iniciar el bucle de eventos de la aplicación
    app.exec()
