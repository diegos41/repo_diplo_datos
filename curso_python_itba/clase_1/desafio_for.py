print('Sistema de impresión de etiquetas')
n_prod= int(input('Ingrese la cantidad de productos diferentes a etiquetar: '))

for x in range (n_prod):
    code= (input('Ingrese el código a imprimir: '))
    t_code= int(input('Ingrese la cantidad de veces que necesita imprimirlo: '))
    for i in range (t_code):
        print(code)



# Utilizando operadores de strings podemos imprimir el output de forma que no quede intercalado con el input
variedad = int(input("Ingrese la variedad de productos:"))
resultado = ""

for x in range(variedad):
    barras = input("Ingrese el codigo de barras correspondiente: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))

    for y in range (cantidad):
      resultado = resultado + barras + '\n'        #\n indica el salto de línea

print(resultado)
     