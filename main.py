# Componenti connesse e MST
# Per studiare gli algoritmi per trovare le componenti connesse si scrivano i seguenti programmi:

# generazione di grafi casuali con un numero di nodi a scelta ed una determinata probabilità di presenza di archi
# tra vertici (es. partire da una matrice di adiacenza con tutti 0 e poi cambiare archi ad 1 con una certa probabilità )
# generazione di grafi pesati casuali

# ricerca delle componenti connesse tramite l'algoritmo di KrusKal o Prim
# Algoritmo di Prim (implementando anche la struttura dati coda con priorità, con min-heap)
# Un programma che permetta di condurre esperimenti su grafi casuali con dimensione crescente e
# con probabilità di presenza di  archi crescente.

# PROGRAMMA DI TEST
import graph

G = graph.Graph(4)
G.random_edges(10)
G.print_graph()

G.prims_mst()
print()
print('MST:')
for i in G.mst:
    print(f'{i[0]} --> {i[1]}')
print()
print(f'Path Cost: {G.weight}')
