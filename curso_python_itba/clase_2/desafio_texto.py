file= open('../noticia.txt', encoding='utf8')                   # ---> ajusté el Path ya que noticia.txt está un directorio arriba.
# Finalmente terminé copiando 'noticia.txt' al mismo directorio. Pero me sirve el cambio de Path para futuros usos.
content= file.readlines()

palabras=[]
no_deseado = ['\n', '"', ',', '.']

for line in content:

    for caracter in no_deseado:
        line= line.replace(caracter, '')
    
    palabras_linea= line.split(' ')
    
    
    for palabra in palabras_linea:
        if palabra != '':
            palabras.append(palabra.lower())

count1=0
count2=0
for palabra in palabras: 
    if palabra=='cráter':
        count1+=1
    elif palabra=='que':
        count2+=1
                
    
print('Cantidad de ocurrencias de la palabra "cráter": ', count1)
print('Cantidad de ocurrencias de la palabra "que": ', count2)

file.close()          #Es una buena práctica "cerrar" el archivo luego de que haya sido abierto.
