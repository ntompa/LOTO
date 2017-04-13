import random

print("Pozdravljen.")

def funkcija_loto():
        velikost = int(input("Vnesi število izbir (< 100): "))
        seznam = []
        i = 0

        while i < velikost:
            x = random.randint(1, 100)         
            if x in seznam:
                continue
            else:
                i += 1
                seznam += [x]

        print()
        print(seznam)
        print()
        print("END")

funkcija_loto()
