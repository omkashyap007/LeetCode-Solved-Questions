class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 33 , 37 , 41 , 43 , 47 , 53 , 57 , 59 , 61 , 67 ])
        count = 0
        for i in range(left ,  right+1):
            if bin(i).count("1") in primes : 
                count += 1
        return count