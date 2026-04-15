print("Repaso Listas")

# Listas (Mutables)
## - Y que se puedan modificar
## - Agregar nuevos elementos
## - Reordenar
## (alumnos, producto de carrito)
## Lista alumnos, lista de los productos dentro del carrito.

#              0       1       2
animales = ["rana", "perro", "gato", "tortuga", "raton", "ajolote", "paloma"]

print(animales)

# Acceso a los datos

print(animales[5])

# Modificación de un dato dentro de una lista

animales[0] = "rana rene"

print(animales[0]) # rana rene
print(animales)

# Recorriendo una lista

for i in range(len(animales)):
    print(i, animales[i])

# Matrices
#            0       1
matriz = [[1, 2], [3, 4]]
#         [0, 1], [0, 1]

print(matriz)

# Acceso a los datos

print(matriz[0][1]) # 2
print(matriz[1][1]) # 4

# Modificar elementos dentro de una matriz
print(matriz)
matriz[0][1] = 22
matriz[1][1] = 44
# matriz = [[1, 22], [3, 44]]
print(matriz)

print(matriz[0][1]) # 22
print(matriz[1][1]) # 44

# ⬇️ ⬇️ <--- columnas
# [1, 2] <--- fila
# [3, 4] <--- fila

## Recorriendo las filaes
for fila in matriz:
    print(fila)

## Recorriendo las filas y columnas
for fila in matriz:
    for valor in fila:
            print(valor)

# Tuplas (inmutables)
# - Los datos no deben cambiar
# - Queremos evitar errores accidentales
# - Coordenadas (x, y)
# - Configuraciones
# - Claves de diccionario
#               0   1
coordenadas = (10, 20)
print(coordenadas)

print(coordenadas[0]) # 10
print(coordenadas[-2]) # 10
print(coordenadas[1]) # 20

config = ("localhost", 5432)

print(config[0])
print(config[1])

for coord in coordenadas:
     print(coord)

## Desestructuración (desempaquetado)
host, port = config

print(host)
print(port)

## Ejemplo real

usuarios = (
     ("maxi", "admin"),
     ("ana", "editor"),
     ("leo", "viewer")
)

print(usuarios)

## recorrer una tupla

for data in usuarios:
    print(data)

# Desestructurando del array usuarios, las claves username, role
for username, role in usuarios:
     print(username, role)

## len(): Nos dice la cantidad de elementos que tengo dentro de una lista o tupla

print(len(animales)) # la cantidad de elementos de la lista
print(len(usuarios)) # la cantidad de elementos de la tupla

# Lista de usuarios, solo puedo acceder a los valores con el índice (o sea la posición)
#            0,       1,       2
listas_usuarios = ["Pedro", "Juan", "Roberto"]

# Una estructura de datos clave -> valor

#                 0    1         2
#                 id, nombre,  role
usuario_maxi_list = [1, "Maxi", "admin"]

# objeto literal de javascript
usuario_maxi_dic = {
     "id": 1,
     "nombre": "Maxi",
     "rol": "admin",
     "direccion": {
          "calle": "Siempre viva",
          "altura": 123
     }
}

# notación corchete de js
print(usuario_maxi_dic["nombre"]) # Maxi
print(usuario_maxi_dic["direccion"]["altura"]) # 123
# print(usuario_maxi_dic["direccion"]["call"]) # KeyError

print(usuario_maxi_dic.get("nombre")) # Más segura la forma de acceder al valor de la clave
print(usuario_maxi_dic.get("nom")) # Si no encuentra la clave devuelve None
# primera forma de recorrer
for key in usuario_maxi_dic:
     print(key, usuario_maxi_dic[key])
# segunda forma de recorrer
for key, value in usuario_maxi_dic.items():
     print(key, value)

print("Fin del programa")