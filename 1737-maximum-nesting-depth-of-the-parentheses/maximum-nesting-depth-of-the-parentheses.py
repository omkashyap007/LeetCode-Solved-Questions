class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        count = 0
        for char in s :
            if char == "(" :
                count += 1
            elif char == ")" :
                count -= 1
            answer = max(count , answer)
        return answer