# Programa para verificar la longitud adecuada de una palabra

# Recibe la palabra del usuario
ingreso_usuario = input("Por favor, ingresa una palabra: ")
tamaño = len(ingreso_usuario)  # Obtiene la longitud de la palabra ingresada

# Evalúa y responde según la longitud de la palabra
if tamaño >= 4 and tamaño <= 8:
    print("La palabra ingresada es correcta.")
elif tamaño < 4:
    print(f"La palabra es demasiado corta. Solo tiene {tamaño} letras.")
else:
    print(f"La palabra es demasiado larga. Tiene {tamaño} letras.")

# Programa para identificar el cuadrante de un punto en base a sus coordenadas

# Recibe las coordenadas del punto del usuario
coordenada_x = float(input("Introduce la coordenada X del punto: "))
coordenada_y = float(input("Introduce la coordenada Y del punto: "))

# Asegura que las coordenadas no sean cero y determina el cuadrante
if coordenada_x == 0 or coordenada_y == 0:
    print("Error: Ninguna de las coordenadas debe ser igual a cero.")
elif coordenada_x > 0 and coordenada_y > 0:
    print("El punto está en el cuadrante I.")
elif coordenada_x < 0 and coordenada_y > 0:
    print("El punto está en el cuadrante II.")
elif coordenada_x < 0 and coordenada_y < 0:
    print("El punto está en el cuadrante III.")
else:
    print("El punto está en el cuadrante IV.")