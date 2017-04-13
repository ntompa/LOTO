#
# resitev s for zanko, kjer v vsakem koraku dodamo en element seznamu izbir
#
import random

print("Pozdravljen.")

def funkcija_loto():
    velikost = int(input("Vnesi število izbir (< 100): "))
    stevila = [i for i in range(1, 101)]
    seznam = []

    for i in range(velikost):
        indeks = random.randint(0, len(stevila) - 1)
        seznam += [stevila[indeks]]
        del stevila[indeks]
    
    print()
    print("sortiran seznam: ", sorted(seznam))
    print()
    print("END")

funkcija_loto()
