class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in hash_map:
                hash_map[key].append(i)
            else:
                hash_map[key] = [i]
        return list(hash_map.values())