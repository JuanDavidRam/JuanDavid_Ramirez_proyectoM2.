# Ejemplo 1
animal = input("Dime un animal: ")
if animal == "perro": 
    print("-Guau.")
elif animal =="gato":
    print("-Miau.")
elif animal =="vaca":
    print("-Muu.")
else:
    print("No conozco su sonido.")
print("conozco pocos animales.")   

# Ejemplo 2
num = int(input("ingresa un numero entero: "))
if num < 0:
    num =-num
print("Su valor absoluto es", num)

# Ejemplo 3
print("impares menores a 10")

x = 1 
while x <=10:
    print(x)
    x+=2

# Ejemplo 4 ciclo while
factorial = 5
contador=factorial - 1
while contador > 0:
    factorial*=contador
    contador-=1