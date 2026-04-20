
# ! Gestión de errores.
# * Errores de sitaxis
## El programa no arranca con estos errores

""" if True
    print("Hola") """

# * Errores en tiempo de ejecución
# El código arranca... me permite ejecutarlo pero explota.

# print(10 / 0)

# * Errores lógicos
# Este error depende de nosotros. Bugs

""" precio = 100
descuento = 20
total = precio - descuento / 100 """

# ? Gestión de errores con try / except
""" print("Inicio de programa")
try:
    # Todx lo que quiero que se ejecute va dentro del try
    # y que puede fallar
    print("Probando...")
    print(10 / 0)
    # otra sentencia
    # otra sentencia
    print("Fin de la prueba probando...")
except ZeroDivisionError:
    print(" No se puede dividir por cero.")
print("Fin de programa") """
""" print("Inicio de programa")
try:
    numero = int(input("Ingrese un número: "))
    print(10 / numero)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Ingresó un valor inválido")
print("Fin de programa") """
""" print("Inicio de programa")
try:
    numero = int(input("Ingrese un número: "))
    print(10 / numero)
except:
    print("Algo se rompió") """

# ! else y finally
# * else: Lo que está en el cuerpo del else se ejecuta solo si el bloque try, está bien y no falla.

try:
    x = int("5") # si sale todo bien
    print(x)
except ValueError:
    print("Error")
else:
    print("Todo OK:", x)

# * finally: No importa lo que ocurra en el try, siempre se va a ejecutar el bloque finally

print("----------------------------")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto se ejecuta sin importantar si hay excepción o no. Siempre")

# Cerrar archivos
# Cerrar conexión de la base de datos
# Liberar recursos
# Logs
