a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a == b == c:
    print("Triángulo equilátero")
elif a == b or a == c or b == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")