class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeroes = 0
        ones = 0
        for i in s :
            if i == "0" :
                zeroes += 1
            else : 
                ones += 1
        s = "1"
        for _ in range(zeroes):
            s += "0"
        for _ in range(ones-1):
            s += "1"
        return s[::-1]