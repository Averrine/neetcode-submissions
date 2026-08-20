class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        #[[1],[1, 2],[1, 2, 3]]
       
        
        for s in strs:
            sortstr = ''.join(sorted(s))
        
            if sortstr in hash:
                hash[sortstr].append(s)
            else:
                hash[sortstr] = [s]
        return list(hash.values())

    
