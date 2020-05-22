
class DisjointSet:
    def __init__(self):
        self.rank = [None] * 10
        self.parent = [None]* 10

    def makeSet(self, item):
        self.rank[item] = 0
        self.parent[item] = item

    def findSet(self, item):
        if self.parent[item] == item:
            return self.parent[item]
        else:
            result = self.findSet(self.parent[item])
            self.parent[item] = result
            return self.findSet(self.parent[item])

    def union(self, set1, set2):
        rep1 = self.findSet(set1)
        rep2 = self.findSet(set2)

        rank1 = self.rank[rep1]
        rank2 = self.rank[rep2]

        if rep1 == rep2:
            return

        if rank1 > rank2:
            self.parent[rep2] = rep1
        elif rank1 < rank2:
            self.parent[rep1] = rep2
        else:
            self.parent[rep2] = rep1
            self.rank[rep1] = 1 + self.rank[rep1]

    def getRankParent(self):
        return (self.rank, self.parent)

set1 = DisjointSet()
for i in range(1,8):
    set1.makeSet(i)

print(set1.getRankParent())

set1.union(1,2)
set1.union(2,3)
set1.union(5,6)
set1.union(6,7)
print(set1.getRankParent())
