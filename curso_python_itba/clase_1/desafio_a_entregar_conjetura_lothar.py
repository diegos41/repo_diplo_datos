print('Conjetura del Dr. Lothar')
nro= int(input('Ingrese un número: '))

j=0
while nro>1:
    j+=1
    if nro%2==0:
        nro=nro/2
    else:
        nro=(nro*3)+1
print(j)