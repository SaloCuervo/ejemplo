peso = float(input("Ingresa tu peso (kg): "))
altura = float(input("Ingresa tu altura (m): "))

imc = peso / (altura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Delgado")
elif 18.5 <= imc < 25:
    print("Peso saludable")
elif 25<= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")