class Solution:

    def check(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.check(s, i+1, j) or self.check(s, i, j-1)
            i += 1
            j -= 1
        return True