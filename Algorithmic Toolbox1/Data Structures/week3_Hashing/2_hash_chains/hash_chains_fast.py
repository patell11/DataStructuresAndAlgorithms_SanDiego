
class HashingWithChains:

    _multiplier = 263
    _prime = 1000000007

    def __init__(self, m):
        self.n_buckets = m
        self.buckets = [[] for _ in range(n_buckets)]

    def hash_fuction(self, string):
        result = 0
        for s in reversed(string):
            result = (result * self._multiplier + ord(s)) % self._prime
        return result % self.n_buckets


    def add(self, string):
        """ If string already present ignore else add to the front in the list chain """
        hashed = self.hash_fuction(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket


    def delete(self, string):
        hashed = self.hash_fuction(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break


    def find(self, string):
        hashed = self.hash_fuction(string)
        bucket = self.buckets[hashed]
        if string in bucket:
            return 'yes'
        return 'no'


    def check(self, value):
        value = int(value)
        return self.buckets[value]


def process(query):
    command, value = query[0], query[1]
    if command == 'add':
        hash_chains.add(value)
    elif command == 'del':
        hash_chains.delete(value)
    elif command == 'check':
        print(" ".join(hash_chains.check(value)))
    elif command == 'find':
        print(hash_chains.find(value))


if __name__ == '__main__':
    n_buckets = int(input())
    n_queries = int(input())
    hash_chains = HashingWithChains(n_buckets)
    for i in range(n_queries):
        query = list(input().split())
        process(query)