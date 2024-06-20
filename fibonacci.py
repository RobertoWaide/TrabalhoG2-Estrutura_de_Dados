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