class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n
        stack = []  # holds indices of temps waiting for a warmer day

        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res

        