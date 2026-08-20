class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # INPUT - int array[nums]
        # OUTPUT - boolean

        if len(nums) != len(set(nums)):
            return True
        return False