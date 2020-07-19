

class BinaryHeap:
    def __init__(self):
        self.heaplist = []
        self.size = 0

    def shiftDown(self, index):
        min_index = index
        left_child_index = 2*index + 1
        right_child_index = 2*index + 2

        if left_child_index < self.size and self.heaplist[min_index] > self.heaplist[left_child_index]:
            min_index = left_child_index
        if right_child_index < self.size and self.heaplist[min_index] > self.heaplist[right_child_index]:
            min_index = right_child_index
        if min_index != index:
            self.heaplist[min_index], self.heaplist[index] = self.heaplist[index], self.heaplist[min_index]
            self.shiftDown(min_index)

    def shiftUp(self, index):
        parent_index = (index -1)//2
        if parent_index >0 and self.heaplist[parent_index] > self.heaplist[index]:
            self.heaplist[parent_index], self.heaplist[index] = self.heaplist[index], self.heaplist[parent_index]
            self.shiftUp(parent_index)


    def extractMin(self):
        min = self.heaplist[0]
        self.heaplist[0] = self.heaplist[self.size-1]
        self.size -= 1
        self.shiftDown(0)
        return min

    def buildHeap(self, alist):
        index_inner_nodes = len(alist)//2
        self.size = len(list)
        self.heaplist = alist
        while index_inner_nodes >= 0:
            self.shiftDown(index_inner_nodes)
            index_inner_nodes -= 1

    def insert(self, val):
        self.heaplist.append(val)
        self.size += 1
        self.shiftUp(self.size -1)

    def remove(self, index):
        self.heaplist[index] = float('-inf')
        self.shiftUp(index)
        self.extractMin()
