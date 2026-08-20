class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # INPUT - two strings: str[s] and str[t]
        # OUTPUT - Boolean 
        ss = ''.join(sorted(s))
        st = ''.join(sorted(t))
        print(st, ss)
        if len(s) == len(t) and ss == st: 
            return True
        return False



