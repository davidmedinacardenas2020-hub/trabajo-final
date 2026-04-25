
cantidad = int(input("¿Cuántos términos deseas ver? "))

primero, segundo = 0, 1
print("=====Ejercicio Fibonacci=====")
for i in range(cantidad):
    print(primero)
    primero, segundo = segundo, primero + segundo