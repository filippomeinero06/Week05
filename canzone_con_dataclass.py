from dataclasses import dataclass

@dataclass(eq=True, order=True)
class Canzone:
    _titolo: str
    _artista: str
    _anno: int (compare = False) # Esclude il campo dall'ordinamento
    _durata: str # "mm:ss"

    # Se diciamo alla dataclass di creare anche i metodi di confronto e ordinamento, vengono creati __eq__()
    # e __lt__() che usano TUTTI GLI ATTRIBUTI

c = Canzone("Titolo", "Artista", 1999, "Durata")
print(c)