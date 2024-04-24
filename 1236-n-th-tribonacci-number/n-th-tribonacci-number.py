class Solution:
    def tribonacci(self, n: int) -> int:
        a , b , c = 0 , 1 , 1
        if n in [0 , 1 ] :
            return n
        if n == 2 :
            return 1
        i = 3
        while i <= n :
            a , b , c = b , c ,  a+b+c
            i += 1
        return c
