# Crear una función que reciba una lista de números y la devuelva:

#   * La suma
#   * El promedio
#   * El número mayor
#   * El número menor

# calcular.py - Vamos a tener 2 archivos (el de la función)
# main.py - Orquesta los modulos

# El resultado esperado luego de la ejecución del programa

# { 'suma': 75, 'promedio': 15.0, 'mayor': 25, 'menor: '5'}

# Valentino

def mostrarLista(lista):
    for i in lista:
        print(i)
def sumaLista(lista):
    return sum(lista)

def promedioLista(lista):
    return sum(lista) / len(lista)
def numeroMayor(lista):
    return max(lista)
def menorNumero(lista):
    return min(lista)

# Nicolas
# -Calcular.py
numeros = [15, 43, 23, 64, 34, 12, 94, 62]
suma = sum(numeros)
promedio = suma / len(numeros)
mayor = max(numeros)
menor = min(numeros)
"""
suma = 0
mayor = numeros[0]
menor = numeros[0]
for n in numeros:
    suma += n
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
"""

# - main.py
print(f"Los numeros son: {numeros}")
print(f"La suma de los numeros es: {suma}")
print(f"El promedio de los numeros de la lista es: {promedio}")
print(f"El numero mayor de la lista es: {mayor}")
print(f"El numero menor de la lista es: {menor}")

# --------------------

# -main.py
numeros = [15, 43, 23, 64, 34, 12, 94, 62]
print(f"Los numeros son: {numeros}")
print(f"La suma de los numeros es: {suma(numeros)}")
print(f"El promedio de los numeros de la lista es: {promedio(numeros)}")
print(f"El numero mayor de la lista es: {mayor(numeros)}")
print(f"El numero menor de la lista es: {menor(numeros)}")

# -calcular.py
def suma(lista):
    return sum(lista)
def promedio(lista):
    return sum(lista) / len(lista)
def mayor(lista):
    return max(lista)
def menor(lista):
    return min(lista)

# Gastón
numeros = [12, 47, 5, 89, 23, 66, 31]
sumar=funciones.suma(numeros)
cantidad_elementos = len(numeros)
promedio= funciones.promedio(sumar, cantidad_elementos)
print("Lista de numeros", numeros)
print("La suma total es: " ,sumar)
print("Promedio: ", promedio)
print("Mayor: ", funciones.mayor(numeros))
print("Menor: ", funciones.menor(numeros))

def suma(numeros):
    total = 0
    for num in numeros:
        total+=num
    return total
def promedio(suma,cantidad):
    return suma/cantidad
def mayor(numeros):
    maximo=numeros[0]
    for num in numeros:
        if num> maximo:
            maximo=num
    return maximo
def menor(numeros):
    menor=numeros[0]
    for num in numeros:
        if num<menor:
            menor=num
    return menor

# Rafael

def procesar_numeros(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    mayor = max(lista)
    menor = min(lista)

    return {
        'suma': suma,
        'promedio': promedio,
        'mayor': mayor,
        'menor': menor
    }

from calcular import procesar_numeros

numeros = [5, 10, 15, 20, 25]

resultado = procesar_numeros(numeros)

print(resultado)

# Lucas

# main.py:
from calcular import sumar, calcular_promedio, buscar_mayor, buscar_menor
print("\n---------------- EJERCICIO ALUMNOS ----------------")
numeros = [60, 40, 10, 80, 30, 50, 20, 70]
suma = sumar(numeros)
promedio = calcular_promedio(numeros)
mayor = buscar_mayor(numeros)
menor = buscar_menor(numeros)
print(f"Suma: {suma} | Promedio: {promedio:.2f} | Mayor: {mayor} | Menor: {menor}")

# calcular.py:
def sumar(lista):
    return sum (lista)
def calcular_promedio(lista):
    return sumar(lista) / len(lista)
def buscar_mayor(lista):
    mayor = lista[0]
    for num in lista[1:]:
        if(num > mayor):
            mayor = num
    return mayor
def buscar_menor(lista):
    menor = lista[0]
    for num in lista[1:]:
        if(num < menor):
            menor = num
    return menor

# calcular.py:
""" def sumar(lista):
    return sum (lista)
def calcular_promedio(lista):
    return sumar(lista) / len(lista)
def buscar_mayor(lista):
    mayor = lista[0]
    for num in lista[1:]:
        if(num > mayor):
            mayor = num
    return mayor
def buscar_menor(lista):
    menor = lista[0]
    for num in lista[1:]:
        if(num < menor):
            menor = num
    return menor """

# Carolina

# Main:
from op import lista, resultado, promedio, mayor, menor
print("La lista ingresada es: ", * lista )
print("Suma=", resultado, ", Promedio=", promedio, ", Mayor=", mayor, ", Menor=", menor)

# * Operaciones
lista = [4,7,2,9,1]

resultado = 0
for i in range(len(lista)):
    resultado = resultado + lista[i]
    promedio = resultado / len(lista)
    mayor = max(lista)
    menor = min(lista)

# Julio
# # main.py
from calcular import sumar_lista, promedio_lista, mayor_lista, menor_lista
mi_lista = [1, 2, 3, 4, 5]
# suma
print('La suma de la lista es :', sumar_lista(mi_lista))
# promedio
print('El promedio de la lista es :', promedio_lista(mi_lista))
# mayor
print('El mayor de la lista es :', mayor_lista(mi_lista))
# menor
print('El menor de la lista es :', menor_lista(mi_lista))

# calcular.py
def sumar_lista(lista):
    if not lista:
        return 0
    suma = 0
    for numero in lista:
        suma += numero
    return suma
def promedio_lista(lista):
    if not lista:
        return None
    suma = sumar_lista(lista)
    return suma / len(lista)
def mayor_lista(lista):
    if not lista:
        return None
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
def menor_lista(lista):
    if not lista:
        return None
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

# Damian

# main.py
from calcular import sumar, promedio, mayor, menor

numeros = [1, 2, 3, 4, 5, 6, 7]

suma = sumar(numeros)
promedio = promedio(numeros)
mayor_val = mayor(numeros)
menor_val = menor(numeros)
print(f"Suma: {suma}, Promedio: {promedio}, Mayor: {mayor_val}, Menor: {menor_val}")
#calcular.py
def sumar(numeros):
    return sum(numeros)

def promedio(numeros):
    return sum(numeros) / len(numeros)

def mayor(numeros):
    return max(numeros)

def menor(numeros):
    return min(numeros)

# Keyla

def lista_numeros(lista):
    mayor = max(lista)
    menor = min(lista)
    suma = sum(lista)
    promedio = suma / len(lista)

    return mayor, menor, suma, promedio

# -----------------

from lista import lista_numeros
lista = [4, 6, 8, 3, 5]
mayor, menor, suma, promedio = lista_numeros(lista)
print("Mayor:", mayor)
print("Menor:", menor)
print("Suma:", suma)
print("Promedio:", promedio)

# Luca

# Luca myejercicio.py
def sumarLista(listaNum):
    res = 0
    for i in range(len(listaNum)):
        res = res + listaNum[i]
    print("Suma de la lista")
    return res

def mayor(listaNum):
    mayor = listaNum[0]
    for i in range(len(listaNum)):
        if listaNum[i] > mayor:
            mayor =listaNum[i]
    print("El mayor de la lista es:")
    return mayor
def menor(listaNum):
    menor = listaNum[0]
    for i in range(len(listaNum)):
        if listaNum[i] < menor:
            menor =listaNum[i]
    print("El menor de la lista es:")
    return menor
def promedio(listaNum):
    res= 0
    for i in range(len(listaNum)):
        res = res + listaNum[i]
    print("El promedio de la lista es:")
    return res/len(listaNum)

#main.py
from operaciones import sumar, restar, multiplicar, dividir
from ejercicioyo.myejercicio import sumarLista,mayor,menor,promedio
listaNum = [1
,2,3,4,5]
sumaLista = sumarLista(listaNum)
print(sumaLista)
print(mayor(listaNum))
print(menor(listaNum))
print(promedio(listaNum))

# Rocio

# Main.py
lista = [4,5,20,10,12]
print("Ejercicio repaso")
resultado_suma = sumar(lista)
resultado_promedio = promedio(lista)
resultado_mayor = mayor(lista)
resultado_menor = menor(lista)
print(f"Suma: {resultado_suma} / Promedio: {resultado_promedio} / Mayor: {resultado_mayor} / Menor: {resultado_menor}")

# calcular.py
def sumar(lista_recibida):
    sum = 0
    i = 0
    while(i<len(lista_recibida)):
        sum = lista_recibida[i] + sum
        i = i + 1
    return sum
def promedio(lista_recibida):
    resul_suma = sumar(lista_recibida) #Reutilizo funcion sumar
    return (resul_suma/len(lista_recibida))

def menor(lista_recibida):
    men = 999999999
    i = 0
    while(i<len(lista_recibida)):
        if(lista_recibida[i]<men):
            men = lista_recibida[i]
        i = i + 1
    return men

def mayor(lista_recibida):
    may = -1
    i = 0
    while(i<len(lista_recibida)):
        if(lista_recibida[i]>may):
            may = lista_recibida[i]
        i = i + 1
    return may

# Diego

#! main.py
from operaciones import sumar,promedio,mayor,menor
numeros = [5,3,4,9,5,8,3,2,5,6]
suma = sumar(numeros)
promedio = promedio(numeros)
mayor = mayor(numeros)
menor = menor(numeros)
resultado = {
    'suma':suma,
    'promedio':promedio,
    'mayor':mayor,
    'menor':menor
}
print(resultado)

#! operaciones.py
def sumar (lista):
    total = 0
    for numero in lista:
        total += numero
    return total
def promedio(lista):
    total = 0
    contador= 0
    for numero in lista:
        total += numero
        contador +=1
    promedio = total/contador
    return promedio
def mayor(lista):
    mayor=lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
def menor(lista):
    menor=lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

# Daniel

def sumar(lista):
    return sum(lista)

def promedio(lista):
    suma = sum(lista)
    cont = len(lista) # dar 0
    if cont > 0:
        prom = (suma / cont)
    return prom

def numero_mayor(lista):
    num_mayor = lista[0]
    for i in lista:
        if i > num_mayor:
            num_mayor = i
    return num_mayor

def numero_menor(lista):
    num_menor = lista[0]
    for i in lista:
        if i < num_menor:
            num_menor = i
    return num_menor

# ----------------------------------------------------------------------------
# [22, 32, 4, 6, 7, 8, 9]
# []
# ['a', 'x', 'nombre', 2, 3, 4]
# ----------------------------------------------------------------------------


from operaciones_danny import sumar, promedio, numero_mayor, numero_menor

lista = [3, 5, 2, 14, 6, 9]
print(sumar(lista))
print(promedio(lista))
print(numero_mayor(lista))
print(numero_menor(lista))

# Franco

def calcular_lista(numeros):
    sumar=0
    may=numeros[0]
    men=numeros[0]
    for num in numeros:
        sumar+=num
        if num > may:
            may = num
        if num < men:
            men= num
    promedio = sumar / len(numeros)
    return f"Suma:{sumar}, Mayor:{may}, Menor:{men}, Promedio: {promedio}"from calcular import calcular_lista
numeros =[1, 2, 3,4,5]
print(calcular_lista(numeros))

# Alex

import random

from calcular import sumar, promediar, maximo, minimo

lista = []

for i in range(6):
    numeros = random.randint(1, 100)
    lista.append(numeros)

print(f"Para la lista: {lista}.")
print(f"suma: {sumar(lista)}, promedio: {promediar(lista)}, mayor: {maximo(lista)}, menor: {minimo(lista)} ")


#MODULO (calcular.py)
def sumar(lista):
    return sum(lista)

def promediar(lista):
    return sum(lista) / len(lista)

def maximo(lista):
    return max(lista)

def minimo(lista):
    return min(lista)
