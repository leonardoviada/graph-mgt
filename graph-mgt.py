"""
---------------------------------------------
	graph-mgt
	v1.0 (Dicembre 2019)

	Libreria di gestione ad oggetti di grafi in Python
	Features:
		# Creazione Grafi
			* Definizione Nodi - Label e Adiacenze
			* Definizione Archi - Peso

		# Applicazione Funzioni di Lettura e Ricerca 
	
---------------------------------------------
	ITIS Delpozzo Cuneo
	Spec. Informatica
	Autore: Leonardo Viada
---------------------------------------------
"""

import random


class Nodo:

    # Costruttore
    def __init__(self, label, adList):
        self.label = label
        self.adList = adList

    # newAd - AGGIUNGE ADIACENZA
    # RICEVE:
    #   label del nodo di destinazione
    #   peso dell'arco da creare - se passiamo solo (label, "rand") viene generato un peso random da 1 a 21 -
    def newAd(self, label, weight):
        if (weight == "rand"):
            weight = random.randrange(1, 21)
        newArco = Arco(label, weight)
        self.adList.append(newArco)

    # Rimuove Adiacenza
    def removeAd(self, nextHop):
        trovato = False
        n = 0
        while (n < len(self.adList) and not trovato):
            if (self.adList[n].nextHop == nextHop):
                trovato = True
                self.adList.pop(n)

    # Cambia Peso Adiacenza
    def editAd(self, nextHop, newWeight):
        trovato = False
        n = 0
        while (n < len(self.adList) and not trovato):
            if (self.adList[n].nextHop == nextHop):
                trovato = True
                self.adList[n].weight = newWeight

    # toString()
    def __str__(self):
        return "label: " + self.label + ", adList: " + str([str(item) for item in self.adList])


class Arco:

    # Costruttore
    def __init__(self, nextHop, weight):
        self.nextHop = nextHop
        self.weight = weight

    # toString()
    def __str__(self):
        return self.nextHop.__str__() + ", " + self.weight.__str__()


# ------
# Main di Prova
# ------

print("Genero i nodi A, B e C...")
A = Nodo("A", [Arco("C", 9)])
B = Nodo("B", [])
C = Nodo("C", [])

print("\nAggiungo adiacenze casuali...")
test = B.newAd("A", "rand")
C.newAd("A", "rand")
C.newAd("B", "rand")
C.newAd("C", "rand")
A.newAd("B", "rand")

print("\nStampo risultati...")
print(A)
print(B)
print(C)

print("\nRimuovo arco fra A e C...")
A.removeAd("C")
print(A)

print("\nModifichiamo il peso dell'arco fra B e A (settiamo a 11)")
B.editAd("A", 11)
print(B)

print("\nGeneriamo un nuovo nodo C...")
D = Arco("B", 6)
print(C)

print("\nAggiungo arco fra B e C, di peso 5...")
B.newAd("C", 5)
print(B)
