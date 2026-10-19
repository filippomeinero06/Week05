# In un modulo dovrebbero esserci le definizioni dei miei dati/tipo di dati, funzioni, ...

LA_MIA_COSTANTE = 67

class LaMiaClasse:
    def __init__(self, attributo):
        self._attributo = attributo

    def funzione(self):
        print("Funzione invocata")

# E' buona norma non scrivere delle cose nei file che definiscono delle funzioni
# print("Questa istruzione è contenuto nel file laMiaClasse.py")

# Codice test della classe (legittimo, ma se qualcuno importa il modulo vengono eseguite anche queste istruzioni)
# prova = LaMiaClasse(56)
# prova.funzione()

# Meglio così:
# Codice di test della classem che però non volgio che venga eseguito quando importo il modulo da un altro
# programma_ basta usare if __name__ == '__main__':
if __name__ == '__main__':
    prova = LaMiaClasse(56)
    prova.funzione()
