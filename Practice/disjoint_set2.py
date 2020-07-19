

class DisjointSet:
    def __init__(self,n):
        self.n = n
        self.rank = [None] * (n+1)
        self.parents = [None] * (n+1)

    def makeSet(self, item):
        self.rank[item] = 0
        self.parents[item] = item

    def findSet(self,item):
        if self.parents[item] == item:
            return self.parents[item]
        self.parents[item] = self.findSet(self.parents[item])

    def union(self, set1, set2):
        rep1 = self.findSet(set1)
        rep2 = self.findSet(set2)

        rank1 = self.rank[rep1]
        rank2 = self.rank[rep2]

        if rep1 == rep2:
            return
        else:
            if rank1 > rank2:
                self.parents[rep2] = rep1
            else:
                self.parents[rep1] = rep2
                if rank1 == rank2:
                    self.rank[rep2] += 1


