print("Esta es la calculadora mirrey del tiempo")
horas , minutos = input("¿Cuántas horas le vas a meter, papu? ") , input("¿Y cuántos minutos? ")
m = float(horas) * 60 
s = float(minutos) * 60
total = m + s
txt = "Son un chingo de segundos. En total {}."
print(txt.format(total))
