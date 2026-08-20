class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        days = 0
        n = len(temps)
        res = [0] * n
        

        for i in range(n): 
            for j in range(i + 1, n):
                if temps[i] < temps[j]:
                    res[i] = j - i
                    break
        return res

        