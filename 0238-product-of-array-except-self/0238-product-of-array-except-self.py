class Solution(object):
    def productExceptSelf(self, nums):
       leftproduct = 1
       rightproduct = 1
       product = [1] * len(nums)
       
       for i in range(len(nums)):
         product[i] = leftproduct     
         leftproduct *= nums[i]

       for i in range(len(nums)-1, -1 , -1):
         product[i] *= rightproduct
         rightproduct *= nums[i]

       return product
         
             
       
        