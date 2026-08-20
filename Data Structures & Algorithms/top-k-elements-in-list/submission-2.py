class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Problem
        # INPUT - int array[nums], int[k]
        # OUTPUT - list of ints

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        for n, freq in count.items():
            buckets[freq].append(n)
        
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


       





        
            






        
        