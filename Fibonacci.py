from collections import deque
import math


class Node():
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False

        # pointers
        self.parent = None
        self.child = None
        self.left = None
        self.right = None


class FibonacciHeap():
    # make-heap
    def __init__(self):
        self.n = 0 # total nodes in Fibonacci heap
        self.min = None
        self.root_list = None # circular, doubly linked list

    def minimum(self):
        return self.min

    def insert(self, key):
        node = Node(key)
        node.left = node
        node.right = node

        self.merge_with_root_list(node)

        if self.min is None or node.key < self.min.key:
            self.min = node 

        self.n += 1
        return node
    
    # merge node with doubly linked root list
    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            # insert at end of root list
            node.right = self.root_list
            node.left = self.root_list.left
            self.root_list.left.right = node
            self.root_list.left = node

    # union of two Fibonacci heaps in O(1)
    def union(self, FH2):
        FH = FibonacciHeap()
        FH.root_list = self.root_list

        # set min to lesser of FH1.min and FH2.min
        FH.min = self.min if self.min.key < FH2.min.key else FH2.min

        # fix pointers to combine root lists
        last = FH2.root_list.left
        FH2.root_list.left = FH.root_list.left
        FH.root_list.left.right = FH2.root_list
        FH.root_list.left = last
        FH.root_list.left.right = FH.root_list

        # update total nodes
        FH.n = self.n + FH2.n

        return FH

    def extract_min(self):
        z = self.min
        if z is not None:
            if z.child is not None:
                # attach child nodes to root list
                children = [x for x in self.iterate(z.child)]
                for i in range(0, len(children)):
                    self.merge_with_root_list(children[i])
                    children[i].parent = None
            self.remove_from_root_list(z)
            # set new min node in heap
            if z == z.right:
                self.min = None
                self.root_list = None
            else:
                self.min = z.right
                self.consolidate()
            self.n -= 1
        return z

def consolidate(self):
        A = [None] * int(math.log(self.n) * 2)
        nodes = [w for w in self.iterate(self.root_list)]
        for w in range(0, len(nodes)):
            x = nodes[w]
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
                    temp = x
                    x, y = y, temp
                self.heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        # find new min node - no need to reconstruct new root list below
        # because root list was iteratively changing as we were moving
        # nodes around in the above loop
        for i in range(0, len(A)):
            if A[i] is not None:
                if A[i].key < self.min.key:
                    self.min = A[i]

# actual linking of one node to another in the root list
    # while also updating the child linked list
    def heap_link(self, y, x):
        self.remove_from_root_list(y)
        y.left = y.right = y
        self.merge_with_child_list(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False

 # merge a node with the doubly linked child list of a root node
    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    # remove a node from the doubly linked root list
    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    # function to iterate through a doubly linked list
    def iterate(self, head):
        node = head
        stop = head
        flag = False

        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    # hacky way of printing the tree
    def print_fibonacci_heap(self, print_marked=False):
        unvisited = deque()
        root_list = []
        marked_nodes = []

        if self.root_list:
            for node in self.iterate(self.root_list):
                root_list.append(node.key)
                unvisited.append(node)

        print('--------------------')
        print('-- Fibonacci Heap --')
        print('--------------------')
        print(f'Total nodes: {self.n}')
        print(f'Minimum: {self.min.key if self.min else None}')
        print(f'Root list node: {self.root_list.key}')
        print(f'Root list: {root_list}')

        while unvisited:
            node = unvisited.popleft()
            if node.mark and (node.key not in marked_nodes):
                marked_nodes.append(node.key)
            if node.child:
                children = []
                for child in self.iterate(node.child):
                    children.append(child.key)
                    if child.child:
                        unvisited.append(child)
                    if child.mark and (child.key not in marked_nodes):
                        marked_nodes.append(child.key)
                print(f'Children of {node.key}: {children}')
        if print_marked:
            print(f'Marked nodes: {marked_nodes}')
        print('--------------------\n')

def insert_example_1():
    FH = FibonacciHeap()

    FH.insert(5)
    FH.insert(2)
    FH.insert(16)
    FH.insert(9)

    FH.print_fibonacci_heap()

