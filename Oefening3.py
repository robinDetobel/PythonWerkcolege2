offertes = []
tot = 0
invoer = float(input("Geef de prijs van de offerte in: "))

while invoer != -1:
    if invoer < 0:
        print("Ongeldig getal ingegeven")
    else:
        offertes.append(invoer)
    invoer = int(input("Geef de prijs van de offerte in: "))

for prijs in offertes:
    tot += prijs

print(tot / len(offertes))