class Canzone:
    def __init__(self, titolo, artista, anno, durata):
        self._titolo = titolo
        self._artista = artista
        self._anno = anno
        self._durata = durata


    def __str__(self):
        return f"{self._titolo} - {self._artista} - {self._anno} - {self._durata}"

    def __repr__(self):
        return f"{self.__class__.__name__}(titolo = '{self._titolo}', artista = '{self._artista}', anno = '{self._anno}', durata = '{self._durata}')"

    # Per consentire a due oggetti di classe Canzone di confrontarsi con == devo andare a ridefinire
    # (in override) nella classe il metodo __eq__(), con l'algoritmo di confronto tra i parametri di self
    # e quelli di other
    def __eq__(self, other):
        if self._titolo == other._titolo and self._artista == other._artista:
            return True
        else:
            return False

    # Analogamente, se voglio che oggetti di tipo Canzone siano ordinabili posso andare a ridefinire
    # (in override) il metodo __lt__()
    def __lt__(self, other):
        # Ordino per anni decrescenti e a parità di anno ordino per durate decrescenti
        if self._anno == other._anno:
            return self._durata > other._durata
        else:
            return self._anno > other._anno

