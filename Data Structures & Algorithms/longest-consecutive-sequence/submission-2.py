class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)

        longest = 0
        for n in hash:
            if (n - 1) not in hash:
                length = 1
                while (n + length) in hash:
                    length += 1
                longest = max(length, longest)
        return longest

        