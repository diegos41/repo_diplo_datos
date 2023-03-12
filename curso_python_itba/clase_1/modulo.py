#Versión de 1 a 365
print("¿Qué dia de la samana cae?")
x= int(input("Ingrese un número de 1 a 365: "))
y= x%7

if y==0:
  print(7)
else:
  print(y)


#Desafío módulo:
print("¿A qué hora llega el corredor a la meta?" )
x= int(input("Ingrese la cantidad de horas: "))
x= x%24
print("Resultado: ", x)