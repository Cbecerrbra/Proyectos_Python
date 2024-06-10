# Se ingresan los valores a las variables agregando las restricciones de los tipos de las variables
def solicitar_cadena(mensaje):
    return input(mensaje)

def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor digita tu edad numérica.")

def solicitar_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor digita tu peso numérico.")

Nombre = solicitar_cadena('Ingresa tu nombre:')
ApellidoPaterno = solicitar_cadena('Ingresa tu apellido paterno:')
ApellidoMaterno = solicitar_cadena('Ingresa tu apellido materno:')
Edad = solicitar_entero('Ingresa tu edad:')
Peso = solicitar_flotante('Ingresa tu peso:')
Estatura = solicitar_flotante('Ingresa tu estatura:')

# Se calcula el índice de masa corporal mediante la formula: peso/estatura2
MasaCorporal = Peso / (Estatura ** 2)

print(f"Tu nombre es {Nombre} {ApellidoPaterno} {ApellidoMaterno} y tu índice de masa corporal es {MasaCorporal}")
