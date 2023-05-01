# Longitud de una frase

palabra = input("Ingresa una palabra: ")

longitud = len(palabra)

if longitud >= 4 and longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print("Hacen falta letras. Solo tiene", longitud, "letras.")
else:
    print("Sobran letras. Tiene", longitud, "letras.")


# Encuentra el cuadrante

otorrinolaringologox = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

if x == 0 or y == 0:
    print("Error: Las coordenadas no pueden ser 0.")
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante 1.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante 2.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante 3.")
else:
    print("El punto se encuentra en el cuadrante 4.")