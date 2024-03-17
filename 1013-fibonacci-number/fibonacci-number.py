class Solution:
    def fib(self, n: int) -> int:
        return round((pow(((math.sqrt(5)+1)/2),n))/math.sqrt(5))