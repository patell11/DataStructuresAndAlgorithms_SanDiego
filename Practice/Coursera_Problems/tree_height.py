

class TreeHeight:
    def read(self):
        self.n = int(input())
        self.parent = list(map(int, input().split()))
        self.depth = [0] * self.n


    def compute_tree_height_naive(self):
        max_height = 0
        for node in range(self.n):
            height = 0
            while node != -1:
                node = self.parent[node]
                height += 1
            max_height = max(height, max_height)
        return max_height

    def compute_tree_height_util(self, index):
        if self.depth[index] != 0:
            return

        if self.parent[index] == -1:
            self.depth[index] = 1
            return

        if self.depth[self.parent[index]] == 0:
            self.compute_tree_height_util(self.parent[index])

        self.depth[index] = self.depth[self.parent[index]] + 1

    def compute_tree_height(self):
        for node in range(self.n):
            self.compute_tree_height_util(node)
        return max(self.depth)

if  __name__ == '__main__':
    tree = TreeHeight()
    tree.read()
    print(tree.compute_tree_height())
