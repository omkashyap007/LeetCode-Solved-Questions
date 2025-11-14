class Solution:
    def maxOperations(self, s: str) -> int:
        answer = 0
        one_count = 0
        i = 0
        while i < len(s):
            if s[i] == "1":
                one_count += 1
                i += 1
            else:
                while i < len(s) and s[i] == "0":
                    i += 1
                answer += one_count
        return answer