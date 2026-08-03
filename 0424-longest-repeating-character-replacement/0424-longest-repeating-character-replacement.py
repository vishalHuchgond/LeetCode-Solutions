class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        count = {}
        max_freq = 0
        ans = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            max_freq = max(max_freq,count[s[i]])
            
            win_size = i- left +1

            while win_size -max_freq > k:
                count[s[left]]-= 1
                left += 1
                win_size = i - left + 1
            ans = max(ans, win_size)
        
        return ans

        