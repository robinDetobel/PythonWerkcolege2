getal = int(input("Geef een getal in: "))
teller = 1
delers = []

while teller < getal:
    if getal%teller == 0:
        delers.append(teller)
    teller += 1
delers.append(getal)

print(delers)