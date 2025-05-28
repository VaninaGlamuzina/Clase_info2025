import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 47)
    intentos = 0
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número del 1 al 47. ¿Puedes adivinar cuál es?")

    while True:
        try:
            adivinanza = int(input("Ingresa tu número: "))
            intentos += 1

            if adivinanza < 1 or adivinanza > 47:
                print("Por favor, elige un número entre 1 y 47.")
            elif adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"🎉 ¡Correcto! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")

juego_adivinanza()