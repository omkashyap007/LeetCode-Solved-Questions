class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1,1001):
            c = 0
            for j in nums :
                if j >= i :
                    c += 1
            if c == i :
                return i
        return -1