import pyodbc as bd
import sys

class Conexion:
    """
    Clase que permite abrir conexión a la BBDD y abrir cursor.
    """
    _SERVIDOR = 'DESKTOP-S935ES7\\SQLEXPRESS01'
    _BBDD = 'ESTUDIANTEDB'
    #_USUARIO = 'app_poo_user'
    #_PASSWORD = '12345678'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene la conexión a la BBDD con los parámetros de conexión pasados como constantes
        """
        if cls._conexion is None:
            try:
                # Utilizando autenticación de Windows -
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';Trusted_Connection=yes')

                # cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                # cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                return cls._conexion
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene un cursor para la conexión a la BBDD.
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                return cls._cursor
            except Exception as e:
                print(e)
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    # Imprimir la conexión obtenida
    print("Conexión:", Conexion.obtenerConexion())

    # Imprimir el cursor obtenido
    print("Cursor:", Conexion.obtenerCursor())
