class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        store = []
        for row in matrix:
            for num in row:
                store.append(num)
                if target in store:
                    return True
        return False


