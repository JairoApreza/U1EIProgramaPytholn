from collections import Counter
texto = 'Hola Mundo De Chairo'
c = texto.split()
archivo = open('C:/Users/Propietario HP/Desktop/SEPTIMO SEMESTRE/PROGRAMACION LOGICA Y FUNCIONAL/Texto.txt', 'r')#Aqui lee el txt
leer = archivo.read()
rx = leer.split()
archivo.close()
a = len(c)

complemento= [None]*a
vueltas = ""

for i in range(0, len(rx)):
    for j in range(0, len(rx)):
        if Counter(rx[i]) == Counter(c[j]):
            complemento[j] = rx[i]

for i in range(0, len(complemento)):
    vueltas += complemento[i]+" "
    print(vueltas)
