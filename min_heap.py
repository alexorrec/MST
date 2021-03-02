import graph


class MinHeap:
    def __init__(self, n):
        self.heap = [graph.Vertex(9999)] * n
        self.size = n
        self.actual_size = -1

    def get_parent_index(self, i):
        return (i - 1) // 2

    def get_left_index(self, i):
        return 2 * i + 1

    def get_right_index(self, i):
        return 2 * i + 2

    def is_empty(self):
        if self.actual_size != 0:
            return True
        else:
            return False

    def is_in(self, value):
        for i in self.heap:
            if i.value == value.value:
                return True
        return False

    def swap(self, index1, index2):
        tmp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = tmp

    def min_heapify(self, i):
        left = self.get_left_index(i)
        right = self.get_right_index(i)
        if left <= self.actual_size and self.heap[left].key < self.heap[i].key:
            min = left
        else:
            min = i
        if right <= self.actual_size and self.heap[right].key < self.heap[min].key:
            min = right
        if min != i:
            self.swap(i, min)
            self.min_heapify(min)

    def extract_min(self):
        if self.size == 0:
            raise ('Empty Heap')
        value = self.heap[0]
        self.heap[0] = self.heap[self.actual_size]
        self.heap.pop(self.actual_size)
        self.actual_size -= 1
        self.min_heapify(0)
        return value

    def decrease_key(self, i, value):
        if value.key > self.heap[i].key:
            raise ('Value bigger')
        self.heap[i] = value
        while i > 0 and self.heap[self.get_parent_index(i)].key > self.heap[i].key:
            self.swap(i, self.get_parent_index(i))
            i = self.get_parent_index(i)

    def insert(self, value):
        self.actual_size += 1
        self.decrease_key(self.actual_size, value)

    def print_heap(self):
        for i in self.heap:
            print(i.value, i.key)
