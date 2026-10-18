class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lm = rm = 0
        water = 0


        while left < right:
            if height[left] < height[right]:
                lm = max(height[left], lm)
                water += lm - height[left]
                left += 1
            else:
                rm = max(height[right], rm)
                water += rm - height[right]
                right -= 1
        return water