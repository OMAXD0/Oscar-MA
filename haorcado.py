import random

def elegir_palabra():
    palabras = ["python", "programacion", "desarrollo", "algoritmo", "computadora"]
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    return ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)

def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    intentos = 6  # Número de intentos permitidos

    print("¡Bienvenido al juego del ahorcado!")
    
    while intentos > 0:
        estado_actual = mostrar_estado(palabra, letras_adivinadas)
        print(f"\nPalabra: {estado_actual}")
        print(f"Tienes {intentos} intentos restantes.")
        
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in palabra:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra.")
        
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break
    else:
        print(f"Has perdido. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar_ahorcado()