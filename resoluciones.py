# Alex
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
altura = float(input("ingrese su altura: "))
estudiante_input = input("¿eres estudiante de educaciónIT? (si/no): ")
estudiante = estudiante_input.lower() == "si"
print (f"hola, {nombre} {apellido}")
print (f"Tu altura es de: {altura}, metros")
if estudiante:
    print("si es estudiante de Educación IT")
else:
    print("No es estudiante de Educación IT")

# Diego
print("Ejercicio 1: Varaibles y tipo")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = float(input("Ingrese su altura en metros: "))
is_student = input("¿Eres estudiante? (si/no): ")
if is_student == "si":
    is_student = True
else:
    is_student = False
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Altura: {altura} metros")
print(f"¿Eres estudiante? {is_student}")

# Florencia
nombre = input("Ingrese su nombre: ")
print(nombre) 
apellido = input("Ingrese su apellido: ")
print(apellido) 
altura = float(input("Ingrese su altura: "))
print(altura) 
sos_estudiante = bool(input("Sos estudiante? ingresa true(SI) o false(NO): "))
print(sos_estudiante) 
mensaje = ""
if sos_estudiante == True:
    mensaje = "sos estudiante"
else: mensaje = "no sos estudiante"
print(f'Hola {nombre} {apellido}, tu altura es de: {altura} metros y {mensaje}')

# Franco
print("-------------INGRESE SUS DATOS------------------")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido:")
altura = float(input("Ingrese su altura (ej: 1.77): "))
estudiante = input("¿sos estudiante?:(Si/NO)")
estudiante = estudiante.lower() == "si"
print("\n")
print("------------DATOS PERSONALES------------")
print("Nombre: ", nombre)
print("Apellido: ", apellido)
print("Su altura es de ", altura," metros")
print("¿es estudiante?: ",estudiante)
print("-------------------------------------")

# Damian
Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Altura = float(input("Ingrese su altura en metros: "))
Es_estudiante = input("¿Sos estudiante? (sí/no): ") == "sí"
print(f"Nombre: {Nombre}, Apellido: {Apellido}, Altura: {Altura}, Es estudiante: {Es_estudiante}")

# Daniel
nombre = input("Escribe aqui tu nombre: ")
apellido = input("Escribe aqui tu apellido: ")
altura = float(input("Escribe aqui tu altura en metros: "))
es_estudiante = True 
respuesta = input("¿Sos estudiante? (si/no)").lower()
es_estudiante = (respuesta == "si")
print(f": {nombre} {apellido} {altura} {es_estudiante}")

# Betania
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = float(input("Ingrese su altura: "))
estudio = input("¿Eres estudiante: ?").capitalize()
if estudio == "Si":
    estudio_new = "Es estudiante"
elif estudio == "No":
    estudio_new = "No es estudiante"
else:
    estudio_new = "No adjunta datos"
datos= (f"Bienvenido {nombre} {apellido}, su altura es: {altura} y {estudio_new}")
print(datos)

# Valentina
print("Ejercicio Uno")
nombre = str(input("ingrese nombre: "))
apellido = str(input("ingrese apellido: "))
altura = float(input("ingrese altura: "))
estudiante = input("ingrese estudiante (Si/No): ").lower() == "si" # Si el usuario ingresa "Si" o "si" o "SI" -> estudiante = True, sino estudiante = False
print("Nombre: " + nombre + " Apellido: " + apellido + " Altura: " + str(altura) + " Estudiante: " + str(estudiante))

# Fernando (2)
moneda = float(input("Ingrese la cantidad de pesos que quiere cambiar a dolares: "))
dolar = moneda/1400
print("con: " + str(moneda) + "pesos y puede comprar: " + str(dolar) + " dolares"  )

# Diana
print("Ejercicio Uno")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = float(input("Ingrese su altura(m2): "))
estudiante = bool(input("¿Es estudiante?: "))
nombre_completo = nombre + " " + apellido
print(nombre_completo)
print(altura)
print(estudiante)

# Nico
nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
altura = float(input("Escriba su estatura: "))
opciones_si = ["si", "sí", "sipi", "obvio", "yes", "s"]
estudiando = input("¿Eres un estudiante?: ").strip().lower() in opciones_si
estudia = "Sí" if estudiando else "No"
print(f"Hola {nombre} {apellido}, mides {altura} Metros, Guau!. ¿Eres estudiante? {estudia}")

# Keyla
nombre = input("ingrese nombre: ")
apellido = input("ingrese apellido: ")
altura = float(input("ingrese altura: "))
estudiante = input("ingrese estudiante (Si/No): ")
print("Nombre: " + nombre + " " + apellido + ". Su altura: " + str(altura) + ". " + estudiante + " es Estudiante")

# Luca
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
altura = float(input("Ingrese su altura en metros(ej:1.77):"))
es_estudiante = bool(input("¿Es estudiante?:").lower() in ['si', 's', 'true', '1'])
print("Nombre:", nombre, "Apellido:", apellido,"Altura:", altura, sep="\n")
if es_estudiante:
    print("Es estudiante")
else:
    print("No es estudiante")