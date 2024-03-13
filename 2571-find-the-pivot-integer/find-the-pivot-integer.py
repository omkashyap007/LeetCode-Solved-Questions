class Solution:

    def isSumEqual(self , x , n):
        one_to_x = ((x*(x+1)))//2
        a = (x-1)
        x_to_n = (n*(n+1))//2 - (a*(a+1))//2
        if one_to_x < x_to_n :
            return -1
        elif one_to_x == x_to_n :
            return 0
        else :
            return 1

    def pivotInteger(self, n: int) -> int:
        l = 1
        r = n
        while l<=r : 
            mid = (l+r)//2
            val = self.isSumEqual(mid , n)
            if val == 0 : 
                return mid
            elif val == -1 :
                l = mid + 1
            else : 
                r = mid -1
        return -1