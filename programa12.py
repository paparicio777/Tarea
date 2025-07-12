#Pedro Aparicio Herrera - 250243
# Presupuesto anual del hospital


# Solicitar el presupuesto anual
presupuesto = float(input("Ingrese el presupuesto anual del hospital: "))

# Calcular presupuesto por área
ginecologia = presupuesto * 0.40
traumatologia = presupuesto * 0.30
pediatria = presupuesto * 0.30

# Mostrar los resultados
print("Presupuesto para Ginecología: $", round(ginecologia, 2))
print("Presupuesto para Traumatología: $", round(traumatologia, 2))
print("Presupuesto para Pediatría: $", round(pediatria, 2))