import random
import min_heap
import node


class Graph:

    def __init__(self, v):
        self.graph = [[0] * v for i in range(v)]  # Questa sarà la matrice contenente i costi degli archi
        self.mst = []
        self.weight = 0
        self.vertex = []  # Lista ordinata di nodi /name
        for i in range(v):
            self.vertex.append(node.Node(i))

    def random_edges(self, n):
        for i in range(n):
            u = random.randint(0, len(self.vertex) - 1) # Nodo
            v = random.randint(0, len(self.vertex) - 1) # Nodo
            w = random.randint(1, 10)                   # Peso
            self.graph[u][v] = w
            self.graph[v][u] = w
            self.graph[u][u] = 0

    def print_graph(self):
        for i in self.graph:
            print(i)

    def prims_mst(self):

        self.vertex[0].key = 0

        # inserisco i nodi nella coda
        Q = min_heap.MinHeap()
        for i in self.vertex:
            Q.insert_heap(i)
        Q.heapify(0)

        while Q.heap:

            u = Q.extract_min()
            self.weight += u.key

            if u.parent is not None:
                self.mst.append([u.parent.name, u.name])

            for i in range(0, len(self.vertex)):
                if self.graph[u.name][i] != 0:
                    if self.vertex[i] in Q.heap and self.graph[u.name][i] < Q.heap[Q.heap.index(self.vertex[i])].key:
                        Q.heap[Q.heap.index(self.vertex[i])].parent = u
                        Q.decrease_key(self.vertex[i], self.graph[u.name][i])
