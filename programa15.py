#Pedro Aparicio Herrera - 250243
# Programa para invertir 3 numeros

print("Puedo invertir tus digitos, ingresa un numero con 3 digitos")
n1= float(input("Ingresa un numero: "))

n2= n1//100
n3= (n1 % 100)//10
n4= n1 % 10
invert= (n4*100)+(n3*10)+n2

print(f"Tu numero invertido es: {invert:.0f}!!!")