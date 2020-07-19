
class BinaryHeap:
    def __init__(self):
        self.heaplst = []
        self.size = 0

    def setHeap(self, alist, size):
        self.heaplst = alist
        self.size = size

    def comparator(self, node1, node2):
        if node1[1] != node2[1]:
            return node1[1] > node2[1]
        else:
            return node1[0] > node2[0]

    def shiftDown(self, index):
        min_index = index
        leftchild = 2*index + 1
        rightchild = 2*index + 2

        if leftchild < self.size and self.comparator(self.heaplst[min_index], self.heaplst[leftchild]):
            min_index = leftchild
        if rightchild < self.size and self.comparator(self.heaplst[min_index], self.heaplst[rightchild]):
            min_index = rightchild
        if min_index != index:
            self.heaplst[index], self.heaplst[min_index] = self.heaplst[min_index], self.heaplst[index]
            self.shiftDown(min_index)

    def changePriority(self, index, new_val):
        old_val = self.heaplst[index][1]
        self.heaplst[index] = (self.heaplst[index][0], new_val)
        if new_val > old_val:
            self.shiftDown(index)
        self.shiftDown(index)



def assign_jobs(n_threads, n_jobs, jobs_lst):
    threads = []
    for i in range(n_threads):
        threads.append((i,0))

    result = []
    thread_heap = BinaryHeap()
    thread_heap.setHeap(threads, n_threads)
    for i in range(n_jobs):
        assigned_thread = thread_heap.heaplst[0]
        result.append((assigned_thread[0], assigned_thread[1]))
        thread_heap.changePriority(0, thread_heap.heaplst[0][1] + jobs_lst[i])

    return result


if __name__ == '__main__':
    n_threads, n_jobs = map(int, input().split())
    jobs_lst = list(map(int, input().split()))

    assigned_threads = assign_jobs(n_threads, n_jobs, jobs_lst)

    for thread, time in assigned_threads:
        print(thread, time)

