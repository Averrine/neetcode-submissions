class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter approach
        '''s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]'''

        # Two pointer approach
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left].lower() not in alpha:
                left += 1
            while right > left and s[right].lower() not in alpha:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True