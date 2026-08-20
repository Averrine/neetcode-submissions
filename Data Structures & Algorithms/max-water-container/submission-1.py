class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        best = 0 
        while left < right:
            h = min(heights[left], heights[right])
            best = max(best, h * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return best
        #[1,7,2,5,4,7,3,6]
        # 0 < 7
        # h = min(1, 6) = 1
        # best = max(0, 1 * (6 - 0))best = 6
        # if 1 < 6
        # 1 < 7
        # h = min(7, 6) = h = 6
        # best = max (5, 6 * (7 - 1)) 6 * 6 = 36
        # best = 36
