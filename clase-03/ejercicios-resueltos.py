# Carolina

# EJ 1:
num = int(input("Ingrese un número: "))
while num <= 0 :
    print("Error!! El número debe ser positivo. Intente nuevamente.")
    num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(i)

# Florencia
print("Ejercicio 1")
numero = int(input("ingrese un numero positivo entero: "))
while numero<= 0:
    numero = int(input("Ingrese un número positivo entero: "))
for i in range(1, numero+1):
    print(i)

#ejericico 2.
# crear un matriz de 3x3 con calificaciones de 3 estudiantes (3 notas cada uno)
# [3, 10, 8]
# [4, 2, 6]
# [8, 7, 6]
#Imprimir:
# cada estudiante con todas sus notas
# el promedio de cada estudiante
print("Ejercicio 2")
matriz = [
    [3, 10, 8], # Fila 0
    [4, 2, 6],  # Fila 1
    [8, 7, 6]   # Fila 2
]
print(matriz)
for fila in matriz:
    total=sum(fila)
    promedio= total / len(fila)
    print(f'promedio: {promedio}')

# Valentina
print("Ejercicio 1")
isnumero = False;
lista = []
while(isnumero == False):
    numero = int(input("Dame numero positivo: "))
    if(numero >= 0):
        isnumero = True
for i in range(numero):
    lista.append(i+1)
print("Numero postivo:", numero)
print("Lista de numeros: ", lista)
print("Ejercicio 2")
#2
matriz = [
    [3, 10, 8],
    [4, 2, 6],
    [8, 7, 6]
]
count= 0
listaPromedios= []
for fila in matriz:
    for valor in fila:
            #print(valor)
            count = count + valor
    print("Estudiante con notas:",fila,"El promedio es: ", count)
    listaPromedios.append(count)
    count = 0
print("Lista de promedios: ", listaPromedios)

# Lucas

numero_positivo = 0
while(numero_positivo <= 0):
    numero_positivo = int(input("Ingrese un numero positivo: "))
for i in range(1, numero_positivo+1):
    print(i, end=" ")

# Damián
#Ejercicio01
print("Ingresa un número positivo:")
n = int(input())
while n <= 0:
    print("Número no válido. Ingresa un número positivo:")
    n = int(input())
for i in range(1, n + 1):
    print(i)

# Betania
while True:
    numero = int(input("Introduce un número mayor a cero: "))
    if numero <= 0:
        print("El número no puede ser negativo o cero")
    else:
        for i in range(numero):
            print(i+1)        #tengo mis dudas con el for

# Alex
import secuencia

numero = int(input("Ingresá un número positivo: "))

while numero <= 0:
    print("Error: El número tiene ser positivo.")
    numero = int(input("Intentá de nuevo: "))

print("La secuencia es:")
secuencia.mostrar_secuencia(numero)


# MODULO (secuencia.py)
def mostrar_secuencia(numero):
    for i in range(1, numero + 1):
        print(i, end=" ")

# Agustín
num = int(input("Ingrese numero: "))
while num <= 0:
    print("ingrese otravez")
    num = int(input("Ingrese otra vez"))
print("Su numero es: ", num)
for i in range (1, num +1):
    print(i)

# Damián
#Ejercicio02
calificaciones = [
    [3, 10, 8],  # Estudiante 1
    [4, 2, 6],   # Estudiante 2
    [8, 7, 6]    # Estudiante 3
]
for i in range(len(calificaciones)):
    estudiante = calificaciones[i]
    print(f"Estudiante {i + 1}: {estudiante}")
    promedio = sum(estudiante) / len(estudiante)
    print(f"Promedio del Estudiante {i + 1}: {promedio:.2f}")

# Carolina
Ej2: matriz = [
    [3, 10, 8],
    [4,2,6],
    [8,7,6]
]
for i in range(len(matriz)):
    notas = matriz[i]
    print(f"Estudiante {i + 1}: {notas}") # "[3, 10, 8]"

    promedio = sum(notas)/ len(notas)
    print(f"Promedio del estudiante: {promedio}\n")

# Franco
print("\n____EJERCICIO 1_____\n")
def pedir_num():
    num=0
    while num<=0:
        num= int(input("Ingrese el numero (mayor a 0):"))
    return num
def retornar_num(num):
    for i in range(1,num+1):
        print(i, end="")

numero = pedir_num()
retornar_num(numero)

print("\n______EJERCICIO 2_____\n")
notas = [
    [3,10, 8],
    [4, 2, 6],
    [8, 7, 6]
]
for i in range(len(notas)):
    print(f"Estudiante {i + 1}: {notas[i]}")

    suma = sum(notas[i])
    promedio = suma / len(notas[i])
    print(f"Promedio: {promedio}\n")

# Gastón
print("EJERCICIO #1")
numero= 0
while numero <=0:
    num_pos = input("ingrese un número posiutivo: ")
    if num_pos.isdigit():
        numero = int(num_pos)
        if numero<=0:
            print("Error, Ingrese numero positivo (mayor a 0)")
    else:
        print("Error, ingrese solo numeros")
#print("Saliste") paso siguiente mostrar numeros dede 1

""" while i<= numero:
    print(i)
    i+=1 """
for i in range(numero):
    print(i+1)

# Elkin
# Ejercicio 1:
i = 0
numero = -5
while i==0:
    numero=int(input("ingrese un numero positivo: "))
    if numero>0:
       i+=1

for i in range(1, numero+1):
        print(i)

# Diego
#! Ejercicio 1

numero = 0
while numero <=0:
    numero = int(input("Escriba un numero positivo: "))
contador = 1
while (contador <= numero):
    print(contador)
    contador = contador + 1


#! Ejercicio 2

estudiante=[
    [3, 10, 8],
    [4, 2, 6],
    [8, 7, 6],
]
for i in  range(len(estudiante)):
    notas = estudiante[i]
    sumas_notas = 0
    for nota in notas:
        sumas_notas = sumas_notas + nota
    promedio = sumas_notas /3
    print(f"estudiante {i+1}: {notas} y promedio : {promedio}")

# Daniel

print("---Ejercicio 1---")
numero = int(input("Ingrese un numero: "))
while (numero <= 0):
    numero = int(input("Ingrese un numero: "))
valor_inicial = 0
for i in range(valor_inicial, numero + 1):
    print(i)

# Melissa
import math

print("Ejercicio 1: ")
print("Ingrese un numero positivo: ")
numero = int(input())
print(" ")

""" while not math.isnan(numero):
    if numero > 0:
        for i in range(1, numero + 1):
            print(i)
        break
    else:
        print("El numero debe ser positivo. Intente nuevamente: ")

    numero = int(input())
    print(" ") """

while numero <= 0:
    print("El numero debe ser positivo. Intente nuevamente: ")
    numero = int(input())

print(" ")
for i in range(1, numero + 1):
    print(i)

print("Ejercicio 2:  \n")

calificaciones = [
    [7, 8, 9],  # Estudiante 1
    [6, 7, 8],  # Estudiante 2
    [9, 10, 10] # Estudiante 3
]

for i in range(len(calificaciones)):
    x = 0
    estudiante = calificaciones[i]
    for nota in estudiante:
        x += 1
    promedio = sum(estudiante) / x
    #Sino, más facil: promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i + 1}: Notas: {estudiante}, Promedio: {promedio:.2f}")

# Nicolas
#ej 1
numero = 0
while numero <= 0:
    numero = int(input("Por favor, ingresa un número positivo: "))
    if numero <= 0:
        print("Dije positivo")
print(f"Secuencia hasta {numero}:")
for i in range(1, numero + 1):
    print(i, end=" ")
print()
print("-" * 30)

# ej 2
matriz_notas = [
    [3, 10, 8],
    [4, 2, 6],
    [8, 7, 6]
]
for i in range(len(matriz_notas)):
    notas = matriz_notas[i]
    promedio = sum(notas) / len(notas)
    print(f"Estudiante {i + 1}:")
    print(f"  Notas: {notas}")
    print(f"  Promedio: {promedio:.2f}")
    print("-" * 30)

# Luca
def contarHasta():
    while True:
        numero = int(input("Ingrese un número positivo: "))
        if numero > 0:
            break
        print("Número no válido. Por favor, ingrese un número positivo.")

    print(f"Números desde 1 hasta {numero}:")
    for i in range(1, numero + 1):
        print(i)


#Ejercicio 2
# Crear una matriz de 3x3 con calificaciones de 3 estudiantes (3 notas cada uno). Imprimir cada estudiante con todas sus notas y el promedio de cada uno
def promediar():
    matriz = [[10,10,10],[5,2,3],[6,7,8]]
    for i in range(3):
        promedio = sum(matriz[i])/len(matriz[i])
        print(f"Estudiante {i}: Notas: {matriz[i]}, Promedio:{promedio}")
