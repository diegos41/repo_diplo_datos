print('Juego del Ahorcado')
palabra = input('Ingrese la palabra a ser adivinada en MAYÚSCULAS: ')

lista_auxiliar = list(palabra)                              # ---> Solo definida para guardar la palabra inicial y mostrarla al final del juego.

for letra in palabra:
    rep = palabra.count(letra)
    if rep>1:
      palabra =  palabra.replace(letra, ' ', rep-1)

#print(palabra)

lista_letras = list(palabra)

#print(lista_letras)

lista_final = []
   
for letra_final in lista_letras:
    if letra_final != ' ':
        lista_final.append(letra_final)

    
#print(lista_final)

attempts = 0
right_guesses = 0

while right_guesses < len(lista_final):
    a_letra = input('Ingrese una letra en MAYÚSCULAS: ')
    attempts += 1
    if a_letra in lista_final:
        right_guesses +=1


print(f"La palabra {''.join(lista_auxiliar)} fue adivinada en {attempts} intentos.")
