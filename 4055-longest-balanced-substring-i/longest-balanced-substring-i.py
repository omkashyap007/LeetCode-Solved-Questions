class Solution:

    def check(self, array, count):
        correct = True
        for i in array:
            if i != 0 and i != count:
                correct = False
                break
        return correct

    def longestBalanced(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            count = [0 for _ in range(26)]
            for j in range(i, len(s)):
                index = ord(s[j]) - ord("a")
                count[index] += 1
                c = count[index]
                if self.check(count, c):
                    answer = max(answer, (j-i+1))
        return answer

