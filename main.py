print("Hola mundo!")

print("Comentario en una línea")

# Una sola línea papá

print("Comentario multilínea")

""" En 
varias 
líneas """

print("Variables")

nombre = "Maxi"
print(nombre) # Cadena

print(type(nombre))

edad = 22
print(edad)

print(type(edad))

is_teacher = True # snake case -> palabra1_palabra2_palabra_3
print(type(is_teacher))
print(is_teacher)
is_teacher = False
print(type(is_teacher))
print(is_teacher)

precio = 33.99
print(type(precio))
print(precio)

# Shortcut -> Play -> Buscar uno que sea comodo para ustedes

print("Concatenación de cadenas")

# Concatenar (juntar texto -> unir textos)

segundo_nombre = "Luis"
apellido = "Principe"

nombre_completo = nombre + " " + segundo_nombre + " " + apellido
print(nombre_completo)

texto = "La" * 3
print(texto) # LaLaLa

print("Función input(): Para pedir datos al usuario")
dato = input("Escribe aquí tu nombre: ")
# print(input("Escribe aquí tu nombre: "))
print(dato)
print("Hola " + dato)
print(f'Hola {dato}') # Otra forma de concatenar (El print tiene caracteristicas para formatear la salida)


print("Casteo (Conversión de tipos)")
print("función int() <-- catea la cadena a un número entero")
cantidad_alumnos = int(input("¿Cuántas alumnos están en clase? "))
print(cantidad_alumnos)
print(type(cantidad_alumnos))
#                       cadena       + numero # ! No se puede concatenar una cadena y un número
cantidad_personas = cantidad_alumnos + 2

print(cantidad_personas) 
print(type(cantidad_alumnos))