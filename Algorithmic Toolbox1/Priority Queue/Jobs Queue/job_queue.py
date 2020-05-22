# python3

class BinaryHeap:
    def __init__(self):
        self.heaplist = []
        self.size = 0

     # compares the time and the worker id - as the worker with the lowest id is prefered over same priority
    def comparator(self, worker1, worker2):
        if worker1[1] != worker2[1]:
            return worker1[1] < worker2[1]
        else:
            return worker1[0] < worker2[0]

    def shiftUp(self, index):
        while index > 0:
            if self.comparator(self.heaplist[index], self.heaplist[(index-1)//2]):
                self.heaplist[index], self.heaplist[(index-1)//2] = self.heaplist[(index-1)//2], self.heaplist[index]
            index = (index-1)//2

    def insert(self, value):
        self.heaplist.append(value)
        self.size = self.size + 1
        self.shiftUp(self.size - 1)

    def shiftDown(self, index):
        min_index = index
        leftchild = 2 * index + 1
        rightchild = 2 * index + 2

        if leftchild < self.size and self.comparator(self.heaplist[leftchild], self.heaplist[min_index]):
            min_index = leftchild
        if rightchild < self.size and self.comparator(self.heaplist[rightchild], self.heaplist[min_index]):
            min_index = rightchild
        if min_index != index:
            self.heaplist[min_index], self.heaplist[index] = self.heaplist[index], self.heaplist[min_index]
            self.shiftDown(min_index)

    def extractMin(self):
        min = self.heaplist[0]
        self.heaplist.pop(0)
        self.size = self.size -1
        return min


    def buildHeap(self):
        i = len(self.heaplist)//2
        while i >= 0:
            self.shiftDown(i)
            i = i-1

    def getHeap(self):
        return self.heaplist

    def setHeaplist(self, alist):
        self.heaplist = alist
        self.size = len(alist)

    """
    Change the priority of the workers based on the time i.e the id with lowest time is given the highest priority
    In the the priority is same, the worker with the lowest id is picked
    """
    def changePriority(self, index, priority_value):
        oldP = self.heaplist[index][1]
        self.heaplist[index] = (self.heaplist[index][0], priority_value)
        if self.heaplist[index][1] > oldP:
            self.shiftDown(index)
        else:
            self.shiftUp(index)
        self.shiftDown(index)

    def setPriority(self,index, priority_value):
        self.heaplist[index][1] = self.heaplist[index][1]+priority_value

def assign_jobs(n_workers, jobs):
    workers = []
    for i in range(n_workers):
        workers.append((i,0))

    result = []
    workers_heap = BinaryHeap()
    workers_heap.setHeaplist(workers)
    for i in range(len(jobs)):
        assigned_thread = workers_heap.heaplist[0]
        result.append((assigned_thread[0], assigned_thread[1]))
        #print(workers_heap.heaplist)  ##
        workers_heap.changePriority(0, workers_heap.heaplist[0][1] + jobs[i])

    return result

#print(assign_jobs(2,[1,2,3,4]))

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for thread, time in assigned_jobs:
        print(thread, time)


if __name__ == "__main__":
    main()
