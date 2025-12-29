class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0 
        i = 0
        j = 0
        hash_map = set()
        while j < len(s):
            if s[j] in hash_map:
                while s[j] in hash_map:
                    hash_map.remove(s[i])
                    i += 1
            answer = max(answer, (j-i+1))
            hash_map.add(s[j])
            j += 1
        return answer
