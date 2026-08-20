class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmm = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hashmm:
                return [hashmm[dif], i]
            hashmm[n] = i
        return []