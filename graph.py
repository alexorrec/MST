import random
import math
import min_heap


class Vertex:
    def __init__(self, cost):
        self.key = cost
        self.value = 0
        self.p = None


class Graph:
    def __init__(self, v, e):
        self.queue = min_heap.MinHeap(v)
        self.graph = [[0] * v for i in range(v)]
        self.edges = e
        self.vertex = [Vertex(999) for i in range(v)]

        c = 0
        for i in self.vertex:
            i.value = c
            c += 1

    def random_edges(self, n):
        for i in range(n):
            u = random.randint(0, self.edges - 1)
            v = random.randint(0, self.edges - 1)
            w = random.randint(1, 10)
            self.graph[u][v] = w
            self.graph[v][u] = w
            self.graph[u][u] = 0

    def print_graph(self):
        for i in self.graph:
            print(i)

    def print_mst(self):
        mst = []
        for i in self.vertex:
            if i.p is not None:
                mst.append(i.p)
        print(mst)

    def prims_mst(self):
        print('MST: ')

        for v in self.vertex:
            self.queue.insert(v)

        self.queue.heap[0].key = 0
        self.queue.decrease_key(0, self.queue.heap[0])
        while self.queue.actual_size != -1:
            u = self.queue.extract_min()  # Oggetto Vertex()
            v_index = -1
            for w in self.graph[u.value]:
                v_index += 1
                if w != 0:
                    if self.queue.is_in(self.vertex[v_index]) and w < self.vertex[v_index].key:
                        self.vertex[v_index].p = u.value
                        self.vertex[v_index].key = w

                        self.queue.decrease_key(v_index, self.vertex[v_index])
