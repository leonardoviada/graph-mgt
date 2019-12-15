
# """
# ---------------------------------------------
#   VERSIONE DI PROVA - LA LIBRERIA E' IN VIA DI SVILUPPO
# ---------------------------------------------
# 	graph-mgt
# 	v1.0 (Dicembre 2019)

# 	Libreria di gestione ad oggetti di grafi in Python
# 	Features:
# 		# Creazione Grafi
# 			* Definizione Nodi - Label e Adiacenze
# 			* Definizione Archi - Peso

# 		# Applicazione Funzioni di Lettura e Ricerca

# ---------------------------------------------
# 	ITIS Delpozzo Cuneo
# 	Spec. Informatica
# 	Autore: Leonardo Viada
# ---------------------------------------------
#  """

import random


class Grafo:

    nodesList = []

    # Costruttore
    def __init__(self, label, nodesList):
        self.label = label
        if(isinstance(nodesList, int)):
            self.seed(nodesList)
        else:
            self.nodesList = nodesList

    # Aggiungi Nuovo Nodo
    def newNode(self, label, adList):
        newNode = Nodo(label, adList)
        self.nodesList.append(newNode)

    def findNodeByLabel(self, label):
        n = 0
        for n in range(len(self.nodesList)):
            if(self.nodesList[n].label == label):
                trovato = True
                return self.nodesList[n]

    def seed(self, nNodes):
        charSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        charSetAvail = []
        for n in range(nNodes):
            temp = charSet[n]
            charSetAvail += temp
            self.newNode(temp, [])
            if(n < nNodes - 1):
                self.nodesList[n].newAd(
                    charSet[n + 1], random.randrange(1, 21))
                for x in range(random.randrange(0, 3)):
                    self.nodesList[n].newAd(random.choice(
                        charSetAvail), random.randrange(1, 21))

    # toString()

    def __str__(self):
        return "label: " + self.label + ", nodesList: " + str([str(item) for item in self.nodesList])


class Arco:

    # Costruttore
    def __init__(self, nextHop, weight):
        self.nextHop = nextHop
        self.weight = weight

    # toString()
    def __str__(self):
        return self.nextHop.__str__() + "-" + self.weight.__str__()


class Nodo:

    # Costruttore
    def __init__(self, label, adList):
        self.label = label
        self.adList = adList

    # newAd - AGGIUNGE ADIACENZA
    # RICEVE:
    #   label del nodo di destinazione
    #   peso dell'arco da creare - se passiamo solo (label, "rand") viene generato un peso random da 1 a 21 -
    def newAd(self, nextHop, weight):
        # TODO: implementare controllo su labels del grafo
        if (weight == "rand"):
            weight = random.randrange(1, 21)
        newArco = Arco(nextHop, weight)
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
                return 0

        return -1

    # Cambia Nome Nodo
    def editLabel(self, newLabel):
        # TODO: implementare controllo su labels del grafo
        self.label = newLabel

    # toString()
    def __str__(self):
        return self.label + ">" + str([str(item) for item in self.adList])