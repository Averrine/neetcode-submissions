class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        if len(strs) == 1:
            return [[strs[0]]]

        for s in strs:
            sortstr = ''.join(sorted(s))
        
            if sortstr in hash:
                hash[sortstr].append(s)
            else:
                hash[sortstr] = [s]
            
        return list(hash.values())
     