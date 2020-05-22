from sys import stdin

## DP approach

## ToDO

def isSubsetSumDP(arr, n, s1, s2):

    matrix = [[[True for z in range(n+1)] for y in range(s1+1)] for x in range(s2+1)]

    for i in range(s1+1):
        for j in range(s2+1):
            for k in range(n+1):
                if j == 0:
                    matrix[i][j][k] = True
                elif (j != 0 and k == 0):
                    matrix[i][j][k] = False
                else:
                    matrix[i][j][k] = matrix[i][j-1]

    return matrix




# A recursive Python3 program for partition problem

# A utility function that returns
# true if there is a subset of
# arr[] with sun equal to given sum
def isSubsetSum(arr, n, s1, s2, memoize_arr):
    #print(memoize_arr)
    # Base Cases
    if (s1 == 0 and s2 == 0) :
        return True
    if n == 0 and (s1 != 0 or s2 != 0):
        return False

    """ The memoize array stores the value and will be used again instead of computing multiple times
        The condition >= 0 is to ignore the indices which can be negative
    """
    if (s1 >= 0 and s2 >= 0):

        if (memoize_arr[n-1][s1-1][s2-1] != -1):
            return memoize_arr[n-1][s1-1][s2-1]

    # print("----Index = ", n)
    # print("part_1 =", arr, n - 1, s1, s2)
    # print("part_2 =", arr, n - 1, s1 - arr[n - 1], s2)
    # print("part_3 =", arr, n - 1, s1, s2 - arr[n - 1])

    ''' else, check if sum can be obtained by any of 
    the following 
    So for three parts each number has three options: either you pick it and put into the first part,
     pick it and put into the second part or you don't pick it and it goes into the first part.
    '''
    if (s1 >= 0 and s2 >= 0):
        memoize_arr[n-1][s1-1][s2-1] = (isSubsetSum(arr, n-1, s1, s2,memoize_arr) or
                                        isSubsetSum(arr, n-1, s1-arr[n-1],s2,memoize_arr) or
                                        isSubsetSum(arr,n-1,s1,s2-arr[n-1],memoize_arr))
        return memoize_arr[n-1][s1-1][s2-1]
    else:
        return (isSubsetSum(arr, n-1, s1, s2,memoize_arr) or
                isSubsetSum(arr, n-1, s1-arr[n-1],s2,memoize_arr) or
                isSubsetSum(arr,n-1,s1,s2-arr[n-1],memoize_arr))


# Returns true if arr[] can be partitioned in three
# subsets of equal sum, otherwise false
def findPartion(arr):
    # Calculate sum of the elements in array
    n = len(arr)
    part_sum = sum(arr)//3
    memoize_arr = [[[-1 for z in range(part_sum + 1)] for y in range(part_sum + 1)] for x in range(n + 1)]
    # If sum is not divisible by 3 or the maximum element in the array is greater than the part_sum or the length is less than 3
    if sum(arr) % 3 != 0 or max(arr) > part_sum or len(arr) < 3:
        return False

    part_sum1 = part_sum
    part_sum2 = part_sum
    return isSubsetSum(arr, n, part_sum1, part_sum2,memoize_arr)


#print(findPartion([7,7,7]))

#Driver program to test above function
# for values, answer in (
#         ((20,), 0),
#         ((7, 7, 7), 1),
#         ((3, 3, 3), 1),
#         ((3, 3, 3, 3), 0),
#         ((3,1,1,2,2),1),
#
# ):
#     print(findPartion(values), answer)




if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    result = findPartion(input_values)
    if result:
        print('1')
    else:
        print('0')
