# crear password
password = input("Ingrese una contraseña que inicie con un número: ")
if not password[0].isdigit():
    print("La contraseña debe iniciar con un número.")
    exit()

intentos = 1
while intentos <= 3:
    password_reingreso = input("Ingrese la contraseña nuevamente: ")
    if password_reingreso == password:
        print("Contraseña confirmada.")
        break
    else:
        print("Las contraseñas no coinciden.")
        intentos += 1

if intentos > 3:
    print("Ha excedido el número máximo de intentos.")
    exit()