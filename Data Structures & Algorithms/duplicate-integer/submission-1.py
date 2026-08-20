class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       

        hashm = []

        for n in nums:
            if n in hashm:
                return True
            else:
                hashm.append(n)
        return False