class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # INPUT - two strings: str[s] and str[t]
        # OUTPUT - Boolean 
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False



