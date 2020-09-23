getal1 = int(input("Geef het eerste getal in: "))
getal2 = int(input("Geef het tweede getal in: "))
teller = 1

if getal1 < getal2:
    while teller < getal1:
        if getal1%teller == 0 and getal2%teller == 0:
            ggd = teller
        teller += 1
else:
    while teller < getal2:
        if getal1%teller == 0 and getal2%teller == 0:
            ggd = teller
        teller += 1

print(ggd)