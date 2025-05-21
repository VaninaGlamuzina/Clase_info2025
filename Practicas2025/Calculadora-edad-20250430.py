anio_actual = 2025
mayor_de_edad = 18

anio_nac = int(input("ingresar año de nacimiento: ")) 

edad_usuario = anio_actual - anio_nac

if (edad_usuario >= mayor_de_edad):
    print("El usuario es mayor de edad")
else:
    print("El usuario NO es mayor de edad")

