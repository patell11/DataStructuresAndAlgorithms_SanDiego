
class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.rank = [None] * (n+1)
        self.parent = [None]* (n+1)

    def makeSet(self, item):
        self.rank[item] = 0
        self.parent[item] = item

    def findSet(self, item):
        if self.parent[item] == item:
            return self.parent[item]
        else:
            result = self.findSet(self.parent[item])
            self.parent[item] = result                ## Path compression
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

    def __str__(self):
        print("i:        ", end=' ')
        for i in range(1, self.n + 1):
            print('{:2d}'.format(i), end=' ')
        print()
        print("parent[i]:", end=' ')
        for p in self.parent[1:]:
            print('{:2d}'.format(p), end=' ')
        print()
        print("rank[i]:  ", end=' ')
        for r in self.rank[1:]:
            print('{:2d}'.format(r), end=' ')
        print()
        return ""

# set1 = DisjointSet()
# for i in range(1,8):
#     set1.makeSet(i)
#
# print(set1.getRankParent())
#
# set1.union(1,2)
# set1.union(2,3)
# set1.union(5,6)
# set1.union(6,7)
# print(set1.getRankParent())

dj = DisjointSet(60)
for i in range(1, 61):
    dj.makeSet(i)
for i in range(1, 31):
    dj.union(i, 2*i)
for i in range(1, 21):
    dj.union(i, 3*i)
for i in range(1, 13):
    dj.union(i, 5*i)
for i in range(1, 61):
    dj.findSet(i)
print(dj)