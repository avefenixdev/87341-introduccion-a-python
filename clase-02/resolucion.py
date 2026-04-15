# Regina
def imprimir(lista):
    for num in lista:
        print(num)
def calcular_suma (lista): 
    suma = 0 # para que no tenga basura
    for num in lista: 
        suma += num
    return suma
""" def calcular_promedio (lista): 
    suma = 0 #para que no tenga basura 
    for num in lista:
       suma += num
    promedio = suma / len(lista)
    return promedio """
def calcular_promedio (suma, lista): 
    promedio = suma / len(lista)
    return promedio
   
import ejercicio

#  Ejercicio: listas
## consigna: crear una lista de numeros y luego: 
# [10,22,55,2,88,7]
# imprimir cada numero (funcion imprimir)
# calcular la suma | suma=calcular_suma (lista) 
# calular promedio | promedio = calcular_promedio (suma, lista)
# al final mostrar la suma y el promedio 
#aca estoy creando mi lista 
lista = [10,22,55,2,88,7] # lista
ejercicio.imprimir(lista) ## Llama e imprime dentro de la función
suma = ejercicio.calcular_suma(lista)
print(ejercicio.calcular_promedio(suma, lista))
print(suma)

# Franco
listanumeros = [10, 22, 55, 2, 88, 7]
print("____MOSTRAR ARRAY___")
for num in (listanumeros):
    print(num)
def calcular_suma(listanumeros):
    total=0
    for num in listanumeros:
        total += num
    return total
suma = calcular_suma(listanumeros)
print(suma)
def calcular_promedio(suma, listanumeros):
   return suma/len(listanumeros)
promedio = calcular_promedio(suma, listanumeros)
print("la suma de todos los numeros es ",suma)
print("el promedio de todos los numeros es:", promedio)

# Elkin
def imprimir(lista):
    for numero in lista:
        print(numero)
    
def calcular_suma(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma
def calcular_promedio(suma, lista):
    promedio = suma/len(lista)
    return promedio

# Melissa

# En "operacion.py"
def calcular_suma(l):
		suma = 0
		for numero in l:
			suma += numero
		return suma

def calcular_promedio(lista):
    cont = 0
    acum = 0
    for numero in lista:
        acum += numero
        cont += 1
    return acum/cont

# En "main.py"
from operacion import calcular_suma, calcular_promedio 

lista = [10, 22, 55, 2, 88, 7]

suma = calcular_suma(lista)

promedio = calcular_promedio(lista)

print("La suma es: ", suma)
print("El promedio es: ", promedio)

# Lucas Iván
import funciones
print("\n---------- EJERCICIO LISTAS ----------")
numeros = [10, 22, 55, 2, 88, 7]
# Mostramos la lista de numeros
print(numeros)
# Calculamos la suma de todos los elemntos de la lista
suma = funciones.calcular_suma(numeros)
# Calculamos el promedio
promedio = funciones.calcular_promedio(suma, numeros)
# Mostramos los datos
print(f"Suma de los numeros: {suma}")
print(f"Promedio: {promedio:.2f}")

def calcular_suma(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma
def calcular_promedio(suma, lista):
    return suma/len(lista)

# Lucas Nahuel
#Modulo Main:
from sumar import calcular_suma, calcular_promedio
numeros = [10, 22, 55, 2, 88, 7]
print(numeros)
for i in range(len(numeros)):
    print(i, numeros[i])
suma = calcular_suma(numeros)
print(f"Suma de los números: {suma}")
promedio = calcular_promedio(suma, numeros)
print(f"Promedio: {promedio}")

#Modulo sumar:
def calcular_suma(lista):
    return sum(lista)
def calcular_promedio(suma, lista):
    if len(lista) == 0:
        return 0
    return suma / len(lista)

# Nicolas
numeritos = [10, 22, 55, 2, 88, 7]

for num in numeritos:
    print(num)
print(numeritos)

def suma(numeros):
    return sum(numeros)

def promedio (numeros):
    return suma(numeros) / len(numeros)

sumado = suma(numeritos)

promediado = promedio(numeritos)

print(sumado)
print(promediado)

# Gastón
# main.py
operacion.imprimir(lista)
print(operacion.suma_lista(lista))
print(operacion.promedio(lista))

# operación.py
def suma_lista(datos):
    sumador = 0
    for dato in datos:
        sumador += dato
    return sumador

def promedio(datos):
    return suma_lista(datos) / len(datos)

def imprimir(datos):
    for dato in datos:
        print(dato)
    
# Romelia
lista_numeros = [10, 22, 55, 2, 88, 7]
def imprimir(lista):
    for num in lista:
        print(num)
""" print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])
print(lista_numeros[3])
print(lista_numeros[4])
print(lista_numeros[5]) """
def sumar(lista):
    sumador = 0 # inicializamos la variable
    for numero in lista:
        sumador += numero
    return sumador
# print(sumar(10, 22, 55, 2, 88, 7))

def calcular_promedio(suma, lista_numeros):
    return suma / len(lista_numeros)

imprimir(lista_numeros) # imprimo la lista
suma = sumar(lista_numeros) # sumo
promedio = calcular_promedio(suma, lista_numeros)
print(suma)
print(promedio)

# Diana
print("*** Ejercicio Listas ***")
lista_numeros = [10, 22, 55, 2, 88, 7]
logica.imprimir_lista(lista_numeros)

total_suma = logica.calcular_suma(lista_numeros)
print("Suma total: ", total_suma)

resultado_promedio = logica.calcular_promedio(total_suma, lista_numeros)
print("Promedio: ", resultado_promedio) 
def imprimir_lista(lista):
    print("Lista:")
    for numero in lista:
        print(numero)
def calcular_suma(lista):
    return sum(lista)
def calcular_promedio(suma, lista):
    if not lista: 
        return 0
    return suma / len(lista)

# Valentino
lista = [10,22,55,2,88,7]
def mostrarLista(lista):
    for i in range(len(lista)):
        print(lista[i])
print(mostrarLista(lista))

def mostrarLista(lista):
    for numero in lista:
        print(numero) # me di cuenta que asi era mas simple.

# Damian
# main.py
import operacion
lista_numeros = [10, 22, 55, 2, 88, 7]
operacion.imprimir(lista_numeros)   
resultado = operacion.suma(lista_numeros)
promedio = operacion.promedio(resultado,lista_numeros)
print(f"La suma es {resultado} y el promedio es {promedio}")

#modulo operacion.py
def suma(lista):
     total = 0
     for numero in lista:
        total += numero
     return total
def promedio(num, lista):
    resultado = num / len(lista)
    return resultado
def imprimir(lista):
    for num in lista:
        print(num)

