
import random

"""
    using the more than one m values to reduce the probability of collision
"""

def preComputeHash(string, m, x):
    string_length = len(string)
    hash_values = [0]
    for i in range(1, string_length + 1):
        val = ((x * hash_values[i - 1]) % m + ord(string[i - 1]) % m) % m
        hash_values.append(val)
    return hash_values


def getHashValue(hash_values, index_start, length, x, m):
    return (hash_values[index_start + length] % m - (pow(x, length, m) * hash_values[index_start]) % m) % m

class SubStringEquality:
    def __init__(self,string):
        self.string = string
        self.m1 = pow(10, 9) + 7
        self.m2 = pow(10, 9) + 9
        self.x = random.randint(1, pow(10, 9))
        self.hash_values_1 = preComputeHash(self.string, self.m1, self.x)
        self.hash_values_2 = preComputeHash(self.string, self.m2, self.x)

    def check(self, index_a, index_b, length):
        hash_value_a1 = getHashValue(self.hash_values_1, index_a, length, self.x, self.m1)
        hash_value_a2 = getHashValue(self.hash_values_2, index_a, length, self.x, self.m2)

        hash_value_b1 = getHashValue(self.hash_values_1, index_b, length, self.x, self.m1)
        hash_value_b2 = getHashValue(self.hash_values_2, index_b, length, self.x, self.m2)

        return (hash_value_a1 == hash_value_b1 and hash_value_a2 == hash_value_b2)

if __name__ == '__main__':
    string = input()
    queries = int(input())
    process = SubStringEquality(string)
    for i in range(queries):
        index_a, index_b, length = map(int, input().split())
        if process.check(index_a, index_b, length):
            print('Yes')
        else:
            print('No')

