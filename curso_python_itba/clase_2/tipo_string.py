nombre= input('Ingrese su nombre: ')
apellido= input('Ingrese su apellido: ')

nombre_y_apellido= nombre + ' ' + apellido

if len(nombre_y_apellido)>26:
    nombre_y_apellido= nombre[0] + ' ' + apellido  
    if len(nombre_y_apellido)>26:
        nombre_y_apellido= nombre[0] + ' ' + apellido[:24]
    
print(nombre_y_apellido)