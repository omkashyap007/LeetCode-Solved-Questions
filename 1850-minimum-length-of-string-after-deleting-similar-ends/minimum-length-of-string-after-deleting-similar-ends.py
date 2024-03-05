class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1 :
            return 1
        l = 0 
        r = len(s)-1
        while l <= r :
            if l == r :
                return 1
            if s[l] == s[r] :
                prev_l = l
                prev_r = r
                while l <= r and s[l] == s[prev_l]  :
                    l += 1
                while r >= l  and s[r] == s[prev_r] :
                    r -= 1
            else : 
                break
        return r-l+1