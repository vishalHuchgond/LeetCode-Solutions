class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        seen = set()
        count = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            count = max(count, right - left + 1)

        return count



        

        