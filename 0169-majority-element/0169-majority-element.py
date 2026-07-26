class Solution(object):
    def majorityElement(self, nums):
        repeated_num = {}

        for num in nums:
            if num not in repeated_num:
                repeated_num[num] = 1
            else:
                repeated_num[num] += 1

            if repeated_num[num] > len(nums) // 2:
                return num 