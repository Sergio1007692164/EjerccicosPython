edad = int(input("digite su edad"))

if edad>=18 and edad<=25:
    print("tiene edad entre 18 y 25")
    if edad>20:
        print("tiene mas de 20")
elif edad>25:
    print("tiene mas de 25")
else:
    print("tiene menos de 18")

