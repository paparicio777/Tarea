#Oliver Alan Moreno Gallegos 250184
# Programa para invertir dos numeros

print("Puedo invertir tus digitos, ingresa un numero de dos digitos")
n1= float(input("Ingresa un numero: "))

n2= n1//10
n3= n1 % 10
invert= (n3*10)+n2

print(f"Tu numero invertido es: {invert:.0f}!!!")
