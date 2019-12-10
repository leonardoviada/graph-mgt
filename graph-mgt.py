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


class Nodo:

    # Costruttore
    def __init__(self, label, adList):
        self.label = label
        self.adList = adList

    # Aggiunge Adiacenza
    def newAd(self, label, weight):
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
A.newAd("B", 4)
B.newAd("A", 3)
C.newAd("A", 7)

print("\nStampo risultati...")
print(A)
print(B)
print(C)

print("\nRimuovo arco fra A e C...")
A.removeAd("C")
print(A)

print("Modifichiamo il peso dell'arco fra B e A - da 3 a 11")
B.editAd("A", 11)
print(B)
