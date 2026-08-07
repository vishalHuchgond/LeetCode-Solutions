class Solution(object):
    def checkInclusion(self, s1, s2):
       str1 = {}
       str2 = {}
       left , right = 0,0
       if len(s1) > len(s2):
         return False
       while right < len(s1):
         ch = s1[right]
         ch1 = s2[right]
         str1[ch] = str1.get(ch, 0) + 1
         str2[ch1] = str2.get(ch1, 0) + 1
         right +=1
       if str1 == str2 :
          return True
       while right < len(s2):
            if str1 == str2 :
                return True
            str2[s2[right]] = str2.get(s2[right], 0) + 1
            str2[s2[left]] = str2.get(s2[left], 0) -1
            if str2[s2[left]] == 0:
                del str2[s2[left]]
            right +=1
            left += 1
            if str1 == str2 :
                return True
              
       return False



