# LONGITUD DE UNA FRASE

# pedimos al usuario que ingrese una palabra y la guardamos en la variable palabra. La función input() se encarga de mostrar el mensaje al usuario y esperar a que ingrese una respuesta.
palabra = input("Ingresa una palabra: ")

# Aquí estamos calculando la longitud de la palabra ingresada por el usuario utilizando la función len(), que devuelve el número de caracteres de una cadena.
longitud = len(palabra)

#En esta parte del código, estamos utilizando una estructura if-elif-else para determinar qué mensaje mostrar al usuario en función de la longitud de la palabra ingresada.
if longitud >= 4 and longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print("Hacen falta letras. Solo tiene", longitud, "letras.")
else:
    print("Sobran letras. Tiene", longitud, "letras.")


# ENCUENTRA EL CUADRANTE
# Pedimos al usuario que ingrese las coordenadas X e Y del punto que desea verificar. La función float() se utiliza para asegurarnos de que las entradas del usuario sean números decimales
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

#En esta parte del código, estamos utilizando una estructura if para verificar si alguna de las coordenadas es igual a 0. Si alguna de las coordenadas es 0, se imprimirá un mensaje de error.
if x == 0 or y == 0:
    print("Error: Las coordenadas no pueden ser 0.")
# En esta parte del código, estamos utilizando una estructura elif para verificar en qué cuadrante se encuentra el punto. Tanto si es mayor o menor.
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante 1.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante 2.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante 3.")
else:
    print("El punto se encuentra en el cuadrante 4.")