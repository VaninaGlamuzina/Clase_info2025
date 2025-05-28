import sys
import os

# Agregar la ruta de carpeta1 al sistema
sys.path.append(os.path.abspath("../modulos"))

# Importar el módulo
import modulo

modulo.saludo()
