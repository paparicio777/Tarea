#Pedro Aparicio Herrera - 250243
#Aumento de salario

# Solicitar el salario anterior al usuario
salario_anterior = float(input("Ingrese el salario anterior: "))

# Calcular el incremento (25%)
incremento = salario_anterior * 0.25

# Calcular el nuevo salario
nuevo_salario = salario_anterior + incremento

# Mostrar el resultado
print("El nuevo salario es: $", round(nuevo_salario, 2))
