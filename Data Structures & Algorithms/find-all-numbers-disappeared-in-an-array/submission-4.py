class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # list = nums of n size
        # nums[i] is in range [1, n]
        # return array of all ints in range [1, n] that are missing
        setNums = set(nums)
        disp = []

        for i in range (1, len(nums) + 1):

            if i not in setNums:
                disp.append(i)
        return disp

