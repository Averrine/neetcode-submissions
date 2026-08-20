class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        #[[1],[1, 2],[1, 2, 3]]
       
        
        for s in strs:
            hash[''.join(sorted(s))].append(s) 
        return list(hash.values())

    
