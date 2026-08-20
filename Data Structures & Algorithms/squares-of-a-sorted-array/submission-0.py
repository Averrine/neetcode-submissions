class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # [nums]
        res = []
        for num in range(len(nums)):
           res.append(nums[num] * nums[num])
           res.sort()
        return res
