def celsius_a_fah(t):
    tf= t*9/5+32 
    return tf

def celsius_a_kel(t):
    tk= t+273.15
    return tk

print('Conversión de temperatura')
tem= int(input('Ingrese la temperatura en °C: '))

while tem<-273.15:
    print('Error.Valor por debajo del cero absoluto.')
    tem= int(input('Ingrese la temperatura nuevamente: '))

print('Temperatura en °F:', celsius_a_fah(tem))
print('Temperatura en K:', celsius_a_kel(tem))

