class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = len(nums)
        
        for i, n in enumerate(nums):

            if i != n:
                return n - 1
            
            if l not in nums:
                return l

            

