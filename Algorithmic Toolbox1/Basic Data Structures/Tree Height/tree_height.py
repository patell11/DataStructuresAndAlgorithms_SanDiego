# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.depth = [0] * self.n

    def compute_height_naive(self):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight

    ## faster approach
    def fill_depth(self,i):
        # base cases

        # if the depth[i] is already filled
        if self.depth[i] != 0:
            return

        # if root node
        if self.parent[i] == -1:
            self.depth[i] = 1
            return

        # If depth of parent is not evaluated before,
        # then evaluate depth of parent first
        if self.depth[self.parent[i]] == 0:
            self.fill_depth(self.parent[i])

        # Depth of this node is depth of parent plus 1
        self.depth[i] = self.depth[self.parent[i]] + 1

    def compute_height(self):

        for i in range(self.n):
            self.fill_depth(i)
        # The height of binary tree is maximum of all depths
        height = max(self.depth)
        return height


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()