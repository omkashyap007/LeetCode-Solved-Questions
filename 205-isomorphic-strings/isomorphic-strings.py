class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        weed_map = {}
        for i in range(len(s)):
            first = s[i]
            second = t[i]
            if first not in hash_map and second not in weed_map :
                hash_map[first] = second
                weed_map[second] = first
            elif first in hash_map and second in weed_map :
                if hash_map[first] != second or weed_map[second] != first : 
                    return False
            elif first in hash_map and second not in weed_map or second in weed_map and first not in hash_map:
                return False
            
        return True