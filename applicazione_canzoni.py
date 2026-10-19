from operator import attrgetter

from canzone import Canzone

c1 = Canzone("Someone like you", "Adele", 2011, "3:11")

c2 = Canzone("Yellow Submarine", "The Beatles", 1966, "4:01")

c3 = Canzone("Scrivile scemo", "Pinguini Tattici Nucleari", 2020, "2:30")

c4 = Canzone("Someone like you", "Altro artista", 2012, "8:10")

if c1 == c4:    # Di default, confronta i riferimenti di c1 e c2
    print("Canzoni uguali")
else:
    print("Canzoni NON uguali")

lista_canzoni = [c1, c2, c3]
lista_canzoni.append(Canzone("Nuova canzone", "Artista", 2020, "8:05"))

print("---------- Lista di canzoni -----------")
for canzone in lista_canzoni:
    print(canzone)

lista_canzoni_ordinata = sorted(lista_canzoni)
print()

print("----------- Lista ordinata per anno -----------")
for canzone in lista_canzoni_ordinata:
    print(canzone)
print()

print("-------- Lista ordinata per titolo -------------")
lista_canzoni_ordinata2 = sorted(lista_canzoni, key=attrgetter('_titolo'), reverse=True)

for canzone in lista_canzoni_ordinata2:
    print(canzone)

print("-------- Lista ordinata per artista -------------")
lista_canzoni_ordinata3 = sorted(lista_canzoni, key=lambda canzone: canzone._artista)

for canzone in lista_canzoni_ordinata3:
    print(canzone)