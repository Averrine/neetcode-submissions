class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # INPUT - input is an int array[nums]
        # OUTPUT - output is a list of lists made up of 3 ints totaling 0, no dups
        # EDGE - empty list

        # O(n^2) time and O(1) space
        # two pointers
        
        # sort
        nums.sort()
        res = []
        # create target to compare sum against
        target = 0
        
        # 1st value aka i
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # skipping any duplicates for i
                continue
            # second and third value aka j and k
            left, right = i + 1, len(nums) - 1

            while left < right:
                # sum to compare against target
                sum = (nums[i] + nums[left] + nums[right])
                # if true
                if sum == target:
                    # all values that equal target
                    triplet = [nums[i], nums[left], nums[right]]
                    # appends those values incase there is multiple triplets that equal 0
                    res.append(triplet)
                    # move pointers
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]: # skip left duplicates
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: # skip duplicates for right
                        right -= 1
                elif sum < target: # if sum is less than 0 move left pointer
                    left += 1
                else: #anything else shift right poitner
                    right -= 1
        # return whatever triplet values we have append to result
        return res  






