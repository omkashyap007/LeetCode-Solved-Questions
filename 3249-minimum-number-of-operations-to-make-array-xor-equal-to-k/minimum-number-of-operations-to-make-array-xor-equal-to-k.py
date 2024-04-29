class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = 0
        for i in nums :
            a^=i
        a = bin(a)[2:]
        k = bin(k)[2:]
        if len(a) > len(k):
            k = (len(a)-len(k))*"0" + k
        if len(a) < len(k):
            a = (len(k)-len(a))*"0" + a
        c = 0
        for i in range(len(a)):
            if a[i] != k[i] :
                c += 1
        return c