print("Ejercicio Pirámide")

cantidad_filas = int(input("¿Cuántas filas quieres? "))

for fila in range(1, cantidad_filas + 1):
    for numero in range(1, fila + 1):
        print(numero, end=" ")
    print()