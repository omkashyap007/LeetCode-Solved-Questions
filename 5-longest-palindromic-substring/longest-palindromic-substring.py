class Solution:
    def longestPalindrome(self , s) :
        
        res = ""
        
        def helper( s , l , r ):
            while l>=0 and r <= len(s)-1 and s[l]==s[r]:
                l-=1 
                r+=1
                
            return s[l+1:r]
        
        for i in range(len(s)) :
            odd = helper(s , i , i)
            even =helper(s , i , i+1)
            
            res = max(odd , even , res , key = len)
        return res