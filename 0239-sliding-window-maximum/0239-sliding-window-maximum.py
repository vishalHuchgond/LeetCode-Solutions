from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        win = deque()
        maximum = []

        left = 0
        right = 0

        while right < len(nums):
            while win and nums[win[-1]] <= nums[right]:
                win.pop()
            win.append(right)
            if win[0] < left:
                win.popleft()
                
            if right - left + 1 == k:
                maximum.append(nums[win[0]])
                left += 1

            right += 1

        return maximum