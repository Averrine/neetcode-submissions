class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashS = set()

        for n in nums:
            if n in hashS:
                return True
            hashS.add(n)
        return False