class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0 
        i = 0
        j = 0
        hash_map = set()
        while j < len(s):
            if s[j] in hash_map:
                while i < j:
                    n = s[i]
                    hash_map.remove(n)
                    i += 1
                    if n == s[j]:
                        break
            curr_len = (j-i+1)
            answer = max(answer, curr_len)
            hash_map.add(s[j])
            j += 1
        return answer
