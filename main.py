""" 
    Esempio di Implementazione con import della libreria
"""


import graphmgt as gmt

print("---\nGenerazione Grafo Casuale\n---")

g = gmt.Grafo("mioGrafo", 11)
print("\n", g)

print("\nAggiungo ad A, un arco verso K di peso 25...")
g.findNodeByLabel("A").newAd("K", 25)
print("\n", g)

print("\nAggiungo a B, un arco verso F di peso 16...")
g.findNodeByLabel("B").newAd("F", 16)
print("\n", g)

print("\nRinomino il nodo K come NODEK")
g.findNodeByLabel("K").editLabel("NODEK")
print("\n", g)
