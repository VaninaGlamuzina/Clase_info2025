class Universidad():
    def __init__(self, nombreUniversidad):
        self.nombreUniversidad = nombreUniversidad

class Carrera():
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, nombre, apellido, edad, nombreUniversidad, especialidad):
        Universidad.__init__(self, nombreUniversidad)
        Carrera.__init__(self, especialidad)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_datos(self):
        print(f"""
              El nombre del estudiante es {self.nombre} y tiene {self.edad} años. 
               Estudia la carrera de {self.especialidad} en la universidad {self.nombreUniversidad} """ )    
        

# Instancia y Ejecucion..

# Paso 1 Crear un estudiante
estudiante1 = Estudiante("Catalina", "Ramirez", 32, "Universidad Nacional del Chaco", "Ingeniería en Sistemas")
# Paso 2 Llamar al método mostrar_datos
estudiante1.mostrar_datos()
