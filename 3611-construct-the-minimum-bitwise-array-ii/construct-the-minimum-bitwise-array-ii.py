class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            if num == 2:
                answer.append(-1)
                continue
            a = -1
            for i in range(1,32):
                if ( num & (1 << i)) > 0:
                    continue
                else:
                    a = num ^ ( 1 << (i-1))
                    break
            answer.append(a)
        return answer
