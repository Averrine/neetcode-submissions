class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CToO = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in CToO:
                if stack and stack[-1] == CToO[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

