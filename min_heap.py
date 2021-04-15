import math


class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return int((i - 1) / 2)

    def get_left(self, i):
        return 2 * i + 1

    def get_right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert_heap(self, node):
        self.heap.append(node)
        # self.heapify(len(self.heap)-1)

    def build_heap(self):
        for i in range(math.floor(len(self.heap) / 2))[::-1]:
            self.heapify(i)

    def heapify(self, i):
        left = self.get_left(i)
        right = self.get_right(i)

        if left <= len(self.heap) - 1 and self.heap[left].key <= self.heap[i].key:
            minimum = left
        else:
            minimum = i
        if right <= len(self.heap) - 1 and self.heap[right].key <= self.heap[minimum].key:
            minimum = right

        if minimum != i:
            self.swap(i, minimum)
            self.heapify(minimum)

    def extract_min(self):
        minimun = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop(len(self.heap) - 1)
        self.heapify(0)
        return minimun

    def print_heap(self):
        print(self.heap)

    def decrease_key(self, node, new_key):
        index = self.heap.index(node)
        self.heap[index].key = new_key

        while index > 1 and self.heap[self.get_parent(index)].key > self.heap[index].key:
            self.swap(index, self.get_parent(index))
            index = self.get_parent(index)
