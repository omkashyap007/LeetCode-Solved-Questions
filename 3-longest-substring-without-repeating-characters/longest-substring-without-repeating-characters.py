class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash_map = {}
        l = r = 0
        max_length = 0
        while r < len(s) :
            hash_map[s[r]] = hash_map.get(s[r],0)+1
            while hash_map[s[r]] > 1 and l < r :
                hash_map[s[l]] -= 1
                l += 1
            max_length = max(max_length , r-l+1)
            r += 1
        return max_length
