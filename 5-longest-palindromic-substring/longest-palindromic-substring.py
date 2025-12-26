class Solution:

    def getPalindrome(self, l, r, s):
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        return s[l:r+1]

    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            odd = self.getPalindrome(i, i, s)
            even = self.getPalindrome(i, i+1, s)
            answer = max(odd, even, answer, key=len)
        return answer