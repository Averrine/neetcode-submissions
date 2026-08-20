class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array of len [n] : rotated between 1 and n times
        

        if nums is not None:
            nums.sort()
            return nums[0]
