nota = int(input("Ingresa la nota (0-100): "))

if 90 <= nota <= 100:
    print("A")
elif 80 <= nota < 90:
    print("B")
elif 70 <= nota < 80:
    print("C")
elif 60 <= nota < 70:
    print("D")
else:
    print("F")