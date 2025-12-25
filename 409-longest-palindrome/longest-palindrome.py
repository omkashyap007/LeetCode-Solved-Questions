class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i, 0)+1
        max_odd = 0
        answer = 0
        take_one = True
        for i in hash_map:
            if hash_map[i]%2 == 1:
                if take_one:
                    answer += 1
                    take_one = False
                answer += hash_map[i]-1
            else:
                answer += hash_map[i]
        return answer + max_odd