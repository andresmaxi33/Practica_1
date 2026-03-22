import random

words = {
    "programacion": ["python", "variable", "funcion"],
    "datos": ["lista", "cadena", "entero"],
    "general": ["programa", "bucle"]
}

score = 0

print("¡Bienvenido al Ahorcado!") 
print()

print("Categorias disponibles:")

for cat in words:
    print("-", cat)
    
while True:
    categoria = input("Elige una categoria: ")
    
    if categoria in words:
        break
    else:
        print("Categoria no valida")

# Lista sin repetir palabras
lista_palabras = random.sample(words[categoria], len(words[categoria]))

for word in lista_palabras:
    
    guessed = []
    attempts = 6
   
    while attempts > 0: 
    # Mostrar progreso: letras adivinadas y guiones para las que faltan 
        progress = "" 
        for letter in word: 
            if letter in guessed: 
                progress += letter + " "
            else: 
                progress += "_ "
        print(progress)
    
    # Verificar si el jugador ya adivinó la palabra completa 
        if "_" not in progress: 
            print("¡Ganaste!") 
            score += 6
            break
    
        print(f"Intentos restantes: {attempts}") 
        print(f"Letras usadas: {', '.join(guessed)}") 
    
        letter = input("Ingresá una letra: ")
    
    #corregir entrada: debe ser una sola letra y no un numero o simbolo
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue
    
        if letter in guessed: 
            print("Ya usaste esa letra.")
        elif letter in word: 
            guessed.append(letter) 
            print("¡Bien! Esa letra está en la palabra.")
        else: 
            guessed.append(letter) 
            attempts -= 1 
            print("Esa letra no está en la palabra.")
            score -= 1

        print()
    
    else: 
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0

print("Puntaje:", score)