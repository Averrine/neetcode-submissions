class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapS = defaultdict(list)
        for s in strs:
            strings = "".join(sorted(s))
            mapS[strings].append(s)
        return list(mapS.values())




            