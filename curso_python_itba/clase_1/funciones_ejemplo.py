def chequarContraseña(c):
    if c == "Secreto":
        resultado = True
    else:
        resultado = False
    return resultado


ingresado = input("Ingrese contraseña: ")        
while not chequarContraseña(ingresado):
    ingresado = input("Contraseña incorrecta. Ingrese de nuevo:")
else:
    print("Contraseña correcta.")