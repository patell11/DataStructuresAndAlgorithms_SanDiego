# python3

import sys
import random
import fileinput

## fro preComputeHash and getHashValue function refer to the 4th program - substring equality
## compute the hash values for all the combinations in the given string
def preComputeHash(string, m, x):
    string_length = len(string)
    hash_values = [0]
    for i in range(1, string_length + 1):
		# subtracting the ASCII code of 'a' to maintain the value of the strings within 0 to 26
        val = ((x * hash_values[i - 1]) % m + (ord(string[i - 1]) - ord('a')) % m) % m
        hash_values.append(val)
    return hash_values

## return the hash value using the precomputed hash values of the given index and length
def getHashValue(hash_values, index_start, length, x, m, power_multiplier):
	return (hash_values[index_start + length] % m - (power_multiplier * hash_values[index_start]) % m) % m


"""
	Precompute power of X with module of M1 and M2. It can buy you extra time when you try 
	to compute hash of substring. Otherwise, it will cost you extra O(log(n)) for pow(X, n, M).
"""
def getPower(x,length,m):
	pow_lst = []
	for i in range(length+1):
		pow_lst.append(pow(x,i,m))
	return pow_lst



class Mismatches:
	def __init__(self, text, pattern):
		self.text = text
		self.pattern = pattern
		self.m1 = pow(10, 15) + 7
		self.m2 = pow(10, 15) + 456
		self.x = 26

		self.pattern_length = len(pattern)

		self.hash_values_t1 = preComputeHash(self.text, self.m1, self.x)
		self.hash_values_t2 = preComputeHash(self.text, self.m2, self.x)

		self.hash_values_p1 = preComputeHash(self.pattern, self.m1, self.x)
		self.hash_values_p2 = preComputeHash(self.pattern, self.m2, self.x)

		self.power_lst_m1 = getPower(self.x, self.pattern_length, self.m1)
		self.power_lst_m2 = getPower(self.x, self.pattern_length, self.m2)

	def solve(self, k, text, pattern):
		pattern_length = len(pattern)
		text_length = len(text)
		result = []
		for i in range(text_length-pattern_length+1):
			value = self.checkMatches(text[i:i+pattern_length], pattern, k, i, i+pattern_length, 0, pattern_length)
			if value <= k:
				result.append(i)
		return result


	def checkMatches(self, subtext, pattern, k, start_index_t, end_index_t, start_index_p, end_index_p):
		mismatch_count = 0

		left = 0
		right = len(pattern)
		mid = left + (right - left)//2
		#print("    ",subtext, pattern, start_index_t, end_index_t, start_index_p, end_index_p)  #left, right, mid, mismatch_count)


		if mid == 0:
			if ord(subtext) != ord(pattern):
				return 1
			else:
				return 0

		if self.checkHash(start_index_t, end_index_t, start_index_p, end_index_p):
			#mismatch_count = mismatch_count + self.checkMatches(subtext[mid:right], pattern[mid:right], k)
			return mismatch_count
		else:
			mid_index_t = (start_index_t + end_index_t)//2  ## uses this index to get the has values of the pattern from the original text
			mid_index_p = (start_index_p + end_index_p)//2  ## keep track of the index for the pattern to get the hash values
			mismatch_count = self.checkMatches(subtext[left:mid], pattern[left:mid], k, start_index_t, mid_index_t, start_index_p, mid_index_p) + \
							 self.checkMatches(subtext[mid:right], pattern[mid:right], k, mid_index_t, end_index_t, mid_index_p, end_index_p)
			return mismatch_count
		#return mismatch_count



	def checkHash(self, index_start_t, index_end_t, index_start_p, index_end_p):
		length = index_end_t - index_start_t
		hash_value_st1 = getHashValue(self.hash_values_t1, index_start_t, length, self.x, self.m1, self.power_lst_m1[length])
		hash_value_st2 = getHashValue(self.hash_values_t2, index_start_t, length, self.x, self.m2, self.power_lst_m2[length])

		hash_value_sp1 = getHashValue(self.hash_values_p1, index_start_p, length, self.x, self.m1, self.power_lst_m1[length])
		hash_value_sp2 = getHashValue(self.hash_values_p2, index_start_p, length, self.x, self.m2, self.power_lst_m2[length])

		return (hash_value_st1 == hash_value_sp1 and hash_value_st2 == hash_value_sp2)


for line in fileinput.input():
	if line != '\n':
		k, t, p = line.split()
		process = Mismatches(t,p)
		ans = process.solve(int(k), t, p)
		print(len(ans), *ans)
