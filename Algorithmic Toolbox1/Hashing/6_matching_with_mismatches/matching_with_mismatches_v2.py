# python2

## ToDo - Implement the binary search to find the number of mismatches

import sys
import random
import fileinput, threading
threading.stack_size(2**27)  # new thread will get stack of such size

## fro preComputeHash and getHashValue function refer to the 4th program - substring equality
## compute the hash values for all the combinations in the given string
def preComputeHash(string, m, x):
    string_length = len(string)
    hash_values = [0]
    for i in range(1, string_length + 1):
        val = ((x * hash_values[i - 1]) % m + ord(string[i - 1]) % m) % m
        hash_values.append(val)
    return hash_values

## return the hash value using the precomputed hash values of the given index and length
def getHashValue(hash_values, index_start, length, x, m):
    return (hash_values[index_start + length] % m - (pow(x, length, m) * hash_values[index_start]) % m) % m

def hashFunction(pattern, _prime, _multiplier):
    hash_value = 0
    for s in reversed(pattern):
        hash_value = ( (hash_value * _multiplier)%_prime + (ord(s)) %_prime ) % _prime
    return hash_value % _prime

def preComputedHasheIndividual(text, n, _prime, _multiplier):
    pattern_length = n
    text_length = len(text)
    hashes = [None] * (text_length - pattern_length + 1)
    last_string = text[text_length - pattern_length:text_length]
    hashes[text_length - pattern_length] = hashFunction(last_string, _prime, _multiplier)

    y = 1
    for i in range(pattern_length):
        y = (y * _multiplier) % _prime

    for i in range(text_length-pattern_length-1, -1, -1):
        hashes[i] = (((hashes[i+1] * _multiplier)%_prime + (ord(text[i]))%_prime - (y * ord(text[i+pattern_length])) % _prime) % _prime) % _prime
    return hashes


class Mismatches:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m1 = pow(10, 7) + 7
        self.m2 = pow(10, 7) + 456
        self.x = random.randint(1, pow(10, 7))

        self.hash_values_t1 = preComputeHash(self.text, self.m1, self.x)
        self.hash_values_t2 = preComputeHash(self.text, self.m2, self.x)

        self.hash_values_p1 = preComputeHash(self.pattern, self.m1, self.x)
        self.hash_values_p2 = preComputeHash(self.pattern, self.m2, self.x)

        #self.mismatch_count = 0

    def solve(self, k, text, pattern):
        pattern_length = len(pattern)
        text_length = len(text)
        result = []
        for i in range(text_length-pattern_length+1):
            value = self.checkMatches(text[i:i+pattern_length], pattern, k, i, i+pattern_length, 0, pattern_length)
            if value <= k:
                result.append(i)
                #print(text[i:i+pattern_length], pattern,value)
        return result

    def checkMatches(self, subtext, pattern, k, start_index_t, end_index_t, start_index_p, end_index_p):

        left = 0
        right = len(pattern)

        while left <= right:
            mid = (left + right)//2
            left_match = self.checkHash()


    def checkHash(self, index_start_t, index_end_t, index_start_p, index_end_p):
        length = index_end_t - index_start_t
        hash_value_st1 = getHashValue(self.hash_values_t1, index_start_t, length, self.x, self.m1)
        hash_value_st2 = getHashValue(self.hash_values_t2, index_start_t, length, self.x, self.m2)

        hash_value_sp1 = getHashValue(self.hash_values_p1, index_start_p, length, self.x, self.m1)
        hash_value_sp2 = getHashValue(self.hash_values_p2, index_start_p, length, self.x, self.m2)

        return (hash_value_st1 == hash_value_sp1 and hash_value_st2 == hash_value_sp2)

print(preComputeHash('abc',10000,20))

#
# def main():
# 	for line in fileinput.input():
# 		if line != '\n':
# 			k, t, p = line.split()
# 			process = Mismatches(t,p)
# 			ans = process.solve(int(k), t, p)
# 			print(len(ans), *ans)
#
# threading.Thread(target=main).start()