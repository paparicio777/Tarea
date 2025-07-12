#Pedro Aparicio Herrera - 250243
#Suma y promedio de 3 numeros 

# Solicitar al usuario que ingrese 3 numeros
num1 = float(input("ingrese el primer numero: "))
num2 = float (input("ingrese el segundo numero: "))
num3 = float (input("ingrese el tercer numero: "))

# Calcular la suma de los numeros
suma = num1 + num2 + num3
prom= suma/3

# Imprimir la suma y el promedio
print (f"la suma de los numeros es: {suma}")
print (f"El promedio de los numeros es: {prom:.2f}")
