# python3

import sys
class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        src_parent_rank = self.ranks[src_parent]
        dst_parent_rank = self.ranks[dst_parent]

        if src_parent == dst_parent:
            return
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size

        if dst_parent_rank > src_parent_rank:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
            # keep in mind when finding the max -  compare the stored max and the value computed in the row_counts list
            # of source/destination index
        else:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
            if dst_parent_rank == dst_parent_rank:
                self.ranks[src_parent] += 1
        return

    def get_parent(self, table):
        # find parent and compress path
        if self.parents[table] != table:
            ## compress the path by updating the parents in the tree
            self.parents[table] = self.get_parent(self.parents[table])

        return self.parents[table]


def main():
    n_tables, n_queries = map(int, sys.stdin.readline().split())
    counts = list(map(int, sys.stdin.readline().split()))
    #assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        #if i % 100 == 0:
         #   print("processing for - ", i)
        dst, src = map(int, sys.stdin.readline().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
