class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        if clean_s == clean_s[::-1]:
            return clean_s == clean_s[::-1]
        else:
            return False
    
    