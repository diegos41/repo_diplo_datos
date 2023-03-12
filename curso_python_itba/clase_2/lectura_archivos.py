file = open("noticia.txt", encoding='utf8') # Guardamos el contenido del archivo en una variable

contenido = file.readlines() # Obtenemos una lista de renglones
#print(contenido)

lista=[]

for line in contenido:
    #print(line)     -->     Mostramos renglón a renglón
    # Eliminamos los distintos carácteres no deseados uno por uno
    line = line.replace('\n','')
    line = line.replace('"','')
    line = line.replace(',','')
    line = line.replace('.','')

    palabras_linea= line.split(' ')       #Separo por espacios (se genera una tupla)
    for palabra in palabras_linea:
        if palabra != '':
            lista.append(palabra)

print(lista)
