"""Programa N°3
coverción de temperatura"""

#Input 
C = input("Dijite el valor de C: ")
C = int(C)

#proccessing
K = C + 273.15
F = 1.8 * C + 32

#Output
print("Grados Farenheit: " + str(F))
print("Grados Kelvin: " + str(K))