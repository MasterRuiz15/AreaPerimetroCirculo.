# Progama para calcular el area y el perimetro de un circulo de radio R

import math

# input
print("------------------------------------")
R = input("Ingrese el valor del radio del circulo: ")
R = int(R)

# processing
A = math.pi*R*R
P = 2*math.pi*R

# output
print("------------------------------------")
print("El area del circulo es: " + str(A))
print("El perimetro del circulo es: " + str(P))
print("------------------------------------")