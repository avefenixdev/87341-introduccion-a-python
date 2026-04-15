print("Condicionales (Tomar decisiones)")

edad = 20
# print("Eres mayor de edad")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# IMPORTANTE TRABAJAR IDENTANDO NUESTRAS SENTENCIAS CUANDO TRABAJO CON BLOQUES
print("-------------------")

if edad >= 18:
    print("Mayor de edad")
    print("Puedes votar")
print("Fin del programa")

print("3 caminos o más con el if")

# nota = 8
nota = int(input("Ingrese una nota de 1 a 10: "))

if nota < 4: 
    print("Desaprobado")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Muy bien")
else:
    print("Excelente")

print("Operadores lógicos")

# and (y lógico)
print("and (y lógico)")

edad = 25
tiene_licencia = True

# a and b = res
# 1     1 = 1 # <---------------------------------------- Ambos verdades
# 1     0 = 0
# 0     1 = 0
# 0     0 = 0


if (edad >= 18 and tiene_licencia):
    print("Puedes manejar")
else:
    print("No puedes manejar")


# or (o lógico)

# a or b = res
# 1     1 = 1 
# 1     0 = 1
# 0     1 = 1
# 0     0 = 0 # <------------- Cuando ambos sean falsos, no se va a cumplir

es_fin_semana = False
es_feriado = False
#      false          true
if es_fin_semana or es_feriado:
    print("No hay clases")
    print("Patino")
else: 
    print("Hay clase")
    print("No patino")

# not (negación o lo opuesto)

# a not
# 1  0
# 0  1

print("Listas: Almacenar varios valores")
""" 
nombre = "Pedro"
nombre2 = "Carlos"
nombre3 = "Ana"
# Es dificil de mantener almacenar 100 personas cada una en una variables
 """

nombres = ["Pedro", "Carlos", "Ana"]

# Listas homogeneas (Recomendables)
## Lista de números
numeros = [10, 20, 30, 40]
## Lista de cadenas
#            0          1          2
frutas = ["manzana", "banana", "naranja"]

# Listas heteregoneas
## Lista mixta
datos = [25, "Maxi", 1.70, True]

# Lista vacía
lista_vacia = []


# Indices empieza en 0, NO EN 1

print(frutas[1]) # banana
print(frutas[2]) # naranja

# Modificando la fruta manzana

frutas[0] = "sandía"

print(frutas)
print(frutas[0])