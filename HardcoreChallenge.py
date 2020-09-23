from math import log10
getal = int(input("Geef een getal in: "))

for i in range(int(log10(getal)),-1,-1):
    val = (getal//(10**i))%10
    if (val != 0):
        print(val)