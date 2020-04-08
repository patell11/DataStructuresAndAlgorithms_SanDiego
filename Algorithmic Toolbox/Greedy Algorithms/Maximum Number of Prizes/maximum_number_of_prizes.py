# python3

#It is not difficult to see that our initial problem has the same type: we need to represent an integer n
#as a sum of the maximum number of pairwise distinct integers each of which is at least 1 (hence k = n and l = 1).
#To summarize, initially we have k = n and l = 1. To solve a (k,l)-sub-problem, we do the following.
#If k ≤ 2l, we output just one summand k. Otherwise we output l and then solve the sub-problem (k−l,l+1).


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []


    num = n
    l = 1
    while num > 0:
        if num <= 2 * l:
            summands.append(num)
            num -= num
            l += 1
        else:
            summands.append(l)
            num = num - l
            l += 1
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)

# for (n, answer) in [(1, 1), (6, 3), (100, 13),(8,3)  ]:
#     output_summands = compute_optimal_summands(n)
#     print(len(output_summands))
#     print(*output_summands)
#     print("\n")
