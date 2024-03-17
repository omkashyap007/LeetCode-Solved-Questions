class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        for i in range(len(s)-1):
            ns = s[i:i+2]
            if len(ns) == 2 and ns in rev :
                return True
        return False