class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        window = {}

        left, right = 0, 0

        if len(t) > len(s):
            return ""

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have, req = 0, len(need)

        result = ""
        result_len = float("inf")

        while right < len(s):

            l = s[right]
            window[l] = window.get(l, 0) + 1

            if l in need and window[l] == need[l]:
                have += 1

            while have == req:

                if right - left + 1 < result_len:
                    result = s[left:right + 1]
                    result_len = right - left + 1

                char = s[left]
                window[char] -= 1

                if char in need and window[char] < need[char]:
                    have -= 1

                left += 1

            right += 1

        return result