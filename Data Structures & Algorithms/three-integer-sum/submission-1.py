class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # INPUT - input is an int array[nums]
        # OUTPUT - output is a list of lists made up of 3 ints totaling 0, no dups
        # EDGE - empty list

        # O(n^2) time and O(1) space
        # two pointers
        nums.sort()
        res = []
        target = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # skipping any duplicates for i
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    triplet = [nums[i], nums[left], nums[right]]
                    res.append(triplet)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
           
        return res  






