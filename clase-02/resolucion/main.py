from utils.promedio import calcular as calcular_promedio
from utils.suma import calcular as calcular_suma

lista = [10, 22, 55, 2, 88, 7]

sumatoria = calcular_promedio(lista)
promedio = calcular_suma(sumatoria, lista)

print(f"La sumatoria es igual: {sumatoria}") 
# Formatear la salida, conviert el print como un template string en js
print(f"El promedio es igual: {promedio}")

