## Desarrolar un programa que imprima el cuadrado del numero que el usuario ingresa mientras que el numero ingresado no sea negativo

a = int(input(print("Ingrese cualquier numero natural: ")))

if (a > 0):
    a = a ** 2
    print("El cuadrado del numero es", a)

else:
    print("El numero es negativo ")

## Ejercicio numero 2

b = int(input(print("Ingrese un número entero positivo: ")))
c = b % 2

if (c != 0):
     b = b * 3 + 1
     while (b >= 2):   
      b = b / 2 
      print(b)     
else:
    while (b >= 2):   
     b = b / 2 
     print("La serie de numero es", b)

## Ejercicio numero 3

año = 2022
Pais_A = 25000000
Pais_B = 18900000

while (Pais_B < Pais_A):
     
     PorcentajeA = Pais_A * 0.2

     Pais_A = PorcentajeA * Pais_A

     PorcentajeB = Pais_B * 0.3

     Pais_B = PorcentajeB * Pais_B

     año = año + 1

print("El año donde el Pais B tiene mayor cantidad de población es", año)