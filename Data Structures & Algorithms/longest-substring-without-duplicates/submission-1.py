class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # var, set, and pointer
        map = set()
        left = 0
        max_length = 0

        # second pointer interating through list
        for right in range(len(s)):
            # checks and removes duplicates
            while s[right] in map:
                map.remove(s[left])
                left += 1
            # adds values to set
            map.add(s[right])
            # picks output interger value between current max_length and the distance between the two pointer, +1 since r - l undercounts
            max_length = max(max_length, right - left + 1)
        return max_length