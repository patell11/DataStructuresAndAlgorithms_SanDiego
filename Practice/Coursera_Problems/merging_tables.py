

class MergeTable:
    def __init__(self, data):
        self.data = data
        self.max_val = max(self.data)
        n_tables = len(data)
        self.rank = [0] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, dst, src):
        rep_dst = self.get_parent(dst)
        rep_src = self.get_parent(src)

        rank_dst = self.rank[rep_dst]
        rank_src = self.rank[rep_src]

        if rep_dst == rep_src:
            return

        if rank_dst > rank_src:
            self.parents[rep_src] = rep_dst
            self.data[rep_dst] += self.data[rep_src]
            self.data[rep_src] = 0
            self.max_val = max(self.max_val, self.data[rep_dst])
        else:
            self.parents[rep_dst] = rep_src
            self.data[rep_src] += self.data[rep_dst]
            self.data[rep_dst] = 0
            self.max_val = max(self.max_val, self.data[rep_src])
            if rank_dst == rank_src:
                self.rank[rep_src] += 1
        return

    def get_parent(self, item):
        if self.parents[item] != item:
            self.parents[item] = self.get_parent(self.parents[item])

        return self.parents[item]


def main():
    n_tables, n_queries = map(int, input().split())
    data = list(map(int, input().split()))
    #assert len(counts) == n_tables
    db = MergeTable(data)
    for i in range(n_queries):
        #if i % 100 == 0:
         #   print("processing for - ", i)
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_val)


if __name__ == "__main__":
    main()
