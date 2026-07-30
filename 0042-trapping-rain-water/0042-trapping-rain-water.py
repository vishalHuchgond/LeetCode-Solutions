class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height)-1
        left_max =0
        right_max = 0
        water_trap = 0
        while left < right:
            left_max = max(left_max , height[left])  
            right_max = max(right_max , height[right])

            if height[left]< height[right]:
                 water_trap += left_max -height[left]
                 left += 1
            else:
                 water_trap += right_max- height[right]
                 right -= 1
        return water_trap