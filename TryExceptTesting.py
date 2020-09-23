offertes = []
tot = 0
invoer = 0

try:
    invoer = float(input("Geef de prijs van de offerte in: "))
except ValueError:
    print("Oops!  Dit was geen getal, probeer het opnieuw.")
except ZeroDivisionError:
    print("Oops!  Dit was geen getal, probeer het opnieuw.")

while invoer != -1:
    if invoer < 0:
        print("Ongeldig getal ingegeven")
    else:
        offertes.append(invoer)
    try:
        invoer = float(input("Geef de prijs van de offerte in: "))
    except ValueError:
        print("Oops!  Dit was geen getal, probeer het opnieuw.")
    except ZeroDivisionError:
        print("Oops!  Dit was geen getal, probeer het opnieuw.")

for prijs in offertes:
    tot += prijs

