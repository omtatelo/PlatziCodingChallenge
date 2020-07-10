print("Esta es la calculadora chola del área de un triángulo.")
base , altura = input("Cáite con la base, prro: ") , input("Ora la altura, prro: ")
b, h = float(base), float(altura)
area = b * h / 2
txt = "Ahí ta: Tu triángulo tiene {} de área :V"
print(txt.format(area))
