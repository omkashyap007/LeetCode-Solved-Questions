class Solution :
    def strStr(self , s , p ):
        answer  = []
        for i in range(len(s)) : 
            k = i
            j = 0
            while j < len(p) and k < len(s)  and s[k] == p[j] : 
                j += 1
                k += 1
            if j == len(p) : 
                return i
        return -1
