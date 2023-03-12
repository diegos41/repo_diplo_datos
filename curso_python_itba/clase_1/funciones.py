def login(user, password):
    if (user=='Juan' and password== '12345_') or (user=='Pablo' and password=='xDcFvGbHn'):
        resultado=True
    else:
        resultado=False
    return resultado

inuser= input('Ingrese el usuario: ')
inpass= input('Ingrese la contraseña: ')

print(login(inuser, inpass))
    