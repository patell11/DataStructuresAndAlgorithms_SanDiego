# python 3

## TODO - optimize - Done

import random
import fileinput
import sys


def binarySearchPattern(pattern, text, _prime1, _prime2, _multiplier):
    pattern_length = len(pattern)
    text_length = len(text)

    left = 0
    right = min(pattern_length, text_length)

    result = None
    longest_substring_result = [(0,1,0)]
    while left <= right:
        mid = left + (right - left)//2
        result = getSubstring(text, pattern, mid, _prime1, _prime2, _multiplier)
        if result[0][2] != 0:
            left = mid +1
        else:
            right = mid -1

        ## Keep track of the longest common substring
        if result[0][2] > longest_substring_result[0][2]:
            longest_substring_result = result

    return longest_substring_result

def hashFunction(pattern, _prime, _multiplier):
    hash_value = 0
    for s in reversed(pattern):
        hash_value = ( (hash_value * _multiplier)%_prime + (ord(s)) %_prime ) % _prime
    return hash_value % _prime

def preComputedHashes(text, n, _prime, _multiplier):
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

def listToDict(lst):
    op = {lst[i]:i for i in range(0, len(lst))}
    return op


def getSubstring(text, pattern, n, _prime1, _prime2, _multiplier):
    """ Using two hash values to reduce the probability of collision """
    result = []
    pattern_hash_value_1 = preComputedHashes(pattern, n, _prime1, _multiplier)
    pattern_hash_value_2 = preComputedHashes(pattern, n, _prime2, _multiplier)

    text_hash_value_1 = preComputedHashes(text, n, _prime1, _multiplier)
    text_hash_value_2 = preComputedHashes(text, n, _prime2, _multiplier)

    # storing into dictionary with map  `hash values` to `start position`
    text_hash_value_1 = listToDict(text_hash_value_1)
    text_hash_value_2 = listToDict(text_hash_value_2)

    for j in range(len(pattern_hash_value_1)):
        if pattern_hash_value_1[j] in text_hash_value_1 and pattern_hash_value_2[j] in text_hash_value_2 :
            result.append((j,text_hash_value_1[pattern_hash_value_1[j]],n))
            return result

    result.append((0,1,0))
    return result



result = []
for line in fileinput.input():
    if line != '\n':
        pattern, text = line.split()
        _prime1 = 1000000039
        _prime2 = 1000000061
        _multiplier = random.randint(1, _prime1-7)
        result = binarySearchPattern(pattern, text, _prime1, _prime2, _multiplier)
        for i in result[0]:
            print(i, end = " ")
        print("\n")
