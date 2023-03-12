a = ["Hola", "Adios", "Como esta", "Buen día" ]
a.sort()
print(a)

#--------------------------------------

b = [1, 2, 3, 123, 23, 12]
b.sort()
print(b)

# Es posible hacer un orden inverso indicando reverse=True
b.sort(reverse=True)
print(b)


#---------------------------------------
# Intercambio de elementos de una lista:
a = [5, 6, 7, 8]
a[0], a[1] = a[1], a[0]            # ---> Acá aparece la tupla.

#---------------------------------------

# En este ejemplo se analiza el segundo valor de cada elemento (y lo utiliza como criterio de orden)
def mi_orden2(e):
  return e[1]

area = [ ["Argentina", 2.78], ["Brazil", 8.51], ["Mexico", 1.96] ]
area.sort(key=mi_orden2)
print("Orden final:", area)

#--------------------------------------

# Matriz utilizando listas. Recordar que se empieza contando desde el 0 para los coeficientes.
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(x[1][2])

#-------------------------------------

#Mini-desafío: Operaciones sobre una lista
print('Ordenador alfabético de nombres')
cant= int(input('Ingrese la cantidad de nombres a ordenar: '))

n_list=[]

for i in range (cant):
    name= input('Ingrese el nombre' + ' ' + str(i+1) + ': ' )
    n_list.append(name)

n_list.sort()

for elemento in n_list:
    print(elemento)