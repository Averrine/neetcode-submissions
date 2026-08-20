class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build prefix and suffix array
        # then multiply by each other
        prefix = [1 for num in range(len(nums))]
        count = 1
        for num in range(len(nums)):
            prefix[num] = count
            count = nums[num] * count
        
        suffix = 1
        for num in range(len(nums) - 1, -1, -1):
            prefix[num] = prefix[num] * suffix
            suffix = suffix * nums[num]
        
        return prefix

        