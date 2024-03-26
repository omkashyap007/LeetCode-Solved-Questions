class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hash_map = {}
        max_length = 0
        for i in s : 
            hash_map[i] = hash_map.get(i , 0)+1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                string = s[i:j+1]
                ok = True
                for char in hash_map:
                    if string.count(char) > 2 :
                        ok = False
                if ok :
                    max_length = max(len(string) , max_length)
        return max_length