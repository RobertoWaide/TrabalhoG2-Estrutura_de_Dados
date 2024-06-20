class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def leftChild(self, i):
        return 2 * i + 1
    
    def rightChild(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.heap.append(key)
        self.heapifyUp(len(self.heap) - 1)
    
    def heapifyUp(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def extractMin(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root
    
    def heapifyDown(self, index):
        smallest = index
        left = self.leftChild(index)
        right = self.rightChild(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapifyDown(smallest)
    
    def getMin(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def leftChild(self, i):
        return 2 * i + 1
    
    def rightChild(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.heap.append(key)
        self.heapifyUp(len(self.heap) - 1)
    
    def heapifyUp(self, index):
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def extractMax(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root
    
    def heapifyDown(self, index):
        largest = index
        left = self.leftChild(index)
        right = self.rightChild(index)
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapifyDown(largest)
    
    def getMax(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(14)
min_heap.insert(9)
print("Min heap:", min_heap.heap)
print("Min element:", min_heap.getMin())
print("Extract min:", min_heap.extractMin())
print("Min heap after extraction:", min_heap.heap)

max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(14)
max_heap.insert(9)
print("Max heap:", max_heap.heap)
print("Max element:", max_heap.getMax())
print("Extract max:", max_heap.extractMax())
print("Max heap after extraction:", max_heap.heap)
