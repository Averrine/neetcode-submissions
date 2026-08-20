class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        if len(strs) == 1:
            return [[strs[0]]]

        for s in strs:
            hash[''.join(sorted(s))].append(s)
        return list(hash.values())
     