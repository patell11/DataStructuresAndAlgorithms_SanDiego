# python 3
import random

def hashFunction(pattern, _prime, _multiplier):
    hash_value = 0
    for s in reversed(pattern):
        hash_value = (hash_value * _multiplier + ord(s)) % _prime
    return hash_value

def preComputedHashes(text, pattern, _prime, _multiplier):
    pattern_length = len(pattern)
    text_length = len(text)
    hashes = [None] * (text_length - pattern_length + 1)
    last_string = text[text_length - pattern_length:text_length]
    hashes[text_length - pattern_length] = hashFunction(last_string, _prime, _multiplier)

    y = 1
    for i in range(pattern_length):
        y = (y * _multiplier) % _prime

    for i in range(text_length-pattern_length-1, -1, -1):
        hashes[i] = (hashes[i+1] * _multiplier + ord(text[i]) - y * ord(text[i+pattern_length])) % _prime

    return hashes

def getOccurences(text, pattern):
    _prime = 1000000007
    _multiplier = random.randint(1, _prime-1)
    result = []
    pattern_length = len(pattern)
    pattern_hashed = hashFunction(pattern, _prime, _multiplier)
    text_hash_value = preComputedHashes(text, pattern, _prime, _multiplier)

    for i in range(len(text_hash_value)):
        if text_hash_value[i] == pattern_hashed:
            if text[i:i+pattern_length] == pattern:
                result.append(str(i))
    return result


if __name__ == '__main__':
    pattern = input()
    text = input()
    print(" ".join((getOccurences(text, pattern))))
