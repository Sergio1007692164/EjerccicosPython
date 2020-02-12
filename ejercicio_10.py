i=1

num = int(input("Digite el valor de num: "))
suma=0
while i<=num:
    nota = float(input("Digite su nota: "))
    suma += nota
    i+=1
print("El promedio es: ", suma/num)
