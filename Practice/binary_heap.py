## Min heap implementation

class BinaryHeap:
    def __init__(self):
        self.heaplist = []
        self.size = 0

    def shiftUp(self, index):
        while index > 0:
            if self.heaplist[index] < self.heaplist[(index-1)//2]:
                temp = self.heaplist[index]
                self.heaplist[index] = self.heaplist[(index-1)//2]
                self.heaplist[(index - 1) // 2] = temp
            index = (index-1)//2

    def insert(self, value):
        self.heaplist.append(value)
        self.size = self.size + 1
        self.shiftUp(self.size - 1)

    def shiftDown(self, index):
        min_index = index
        leftchild = 2 * index + 1
        rightchild = 2 * index + 2

        if leftchild < self.size and self.heaplist[min_index] > self.heaplist[leftchild]:
            min_index = leftchild
        if rightchild < self.size and self.heaplist[min_index] > self.heaplist[rightchild]:
            min_index = rightchild
        if min_index != index:
            temp = self.heaplist[index]
            self.heaplist[index] = self.heaplist[min_index]
            self.heaplist[min_index] = temp
            self.shiftDown(min_index)

    def extractMin(self):
        min = self.heaplist[0]
        self.heaplist[0] = self.heaplist[self.size -1]
        self.size = self.size -1
        self.shiftDown(0)
        return min

    def inplace_sort(self):
        while self.size > 0:
            self.heaplist[0],self.heaplist[self.size-1] = self.heaplist[self.size-1], self.heaplist[0]
            self.size = self.size -1
            self.shiftDown(0)
        return self.heaplist


    def remove(self, index):
        self.heaplist[index] = float('-inf')
        self.shiftUp(index)
        self.extractMin()

    def buildHeap(self,alist):

        i = len(alist)//2
        self.heaplist = alist
        self.size = len(alist)
        while i >= 0:
            self.shiftDown(i)
            i = i-1

    def setHeapList(self, alist):
        self.heaplist = alist

    def getHeap(self):
        return self.heaplist
#
# bh = BinaryHeap()
# bh.buildHeap([9,5,6,2,3])
#
# print(bh.getHeap())
# print(bh.extractMin())
# print(bh.extractMin())
# print(bh.extractMin())
# print(bh.extractMin())
# print(bh.extractMin())


