import operacion
from logica import calcular_doble, calcular_triple as triple
from logica import * # evitarlo
# Modulos y funciones
# Se puede poner una alias a la función del modulo que estoy incorporando, lo hago con as

# Una función en python se crea a partir de la palabra reservada def

# función javascript
""" function sumar(a, b) {
    return a + b
} """

def sumar(a, b):
    return a + b

print(sumar(4, 4)) # 8

print(operacion.sumar_modulo(4, 2))
print(operacion.resta_modulo(10, 7))

print(calcular_doble(50))

print(triple(10))