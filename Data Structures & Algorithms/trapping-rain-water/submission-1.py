class Solution:
    def trap(self, height: List[int]) -> int:
        # Input - int array [height]
    
        left, right = 0, len(height) - 1
        maxl = maxr = water = 0
        while left < right:
            if height[left] < height[right]:
                maxl = max(maxl, height[left])
                water += maxl - height[left]
                left += 1
            else:
                maxr = max(maxr, height[right])
                water += maxr - height[right]
                right -=1
        return water
