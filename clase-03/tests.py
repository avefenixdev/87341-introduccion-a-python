print("Inicio de programa")
while True:
    numero = int(input("Introduce un número mayor a cero: "))
    if numero <= 0:
        print("El número no puede ser negativo o cero")
        continue
    else:
        for i in range(numero):
            print(i+1)        #tengo mis dudas con el for
        break
print('Fin del programa')
