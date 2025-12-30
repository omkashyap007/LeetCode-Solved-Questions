class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        max_frequency = 0
        hash_map = defaultdict(int)
        i = j = 0
        while j < len(s):
            hash_map[s[j]] += 1
            max_frequency = max(max_frequency, hash_map[s[j]])
            while (j-i+1) - max_frequency > k:
                hash_map[s[i]] -= 1
                i += 1
            answer = max(answer, (j-i+1))
            j += 1
        return answer
