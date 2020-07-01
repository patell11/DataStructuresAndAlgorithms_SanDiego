class Solution:
    def binarySearch(item, nums):
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == item:
                return (True, mid)
            else:
                if nums[mid] > item:
                    right = mid - 1
                else:
                    left = mid + 1
        return False, -1


    def twoSum(self, nums ,target):
        for i in range(len(nums)):
            first_part = nums[i]
            second_part = target - first_part
            found, index = self.binarySearch(second_part, nums)
            if found and index != i:
                return [i, index]




if __name__ == '__main__':
    alist = input()
    target_sum = int(input())
    two_sum = Solution()
    print(two_sum.twoSum(alist, target_sum))

    ten_power1 = 0
    num1 = 0
    while l1.next != None:
        num1 = num1 + (l1.val * (10 ** ten_power1))
        ten_power1 += 1
        l1.next = next

    ten_power2 = 0
    num2 = 0
    while l2.next != None:
        num2 = num2 + (l2.val * (10 ** ten_power2))
        ten_power2 += 1
        l2.next = next

    return (num1 + num2)