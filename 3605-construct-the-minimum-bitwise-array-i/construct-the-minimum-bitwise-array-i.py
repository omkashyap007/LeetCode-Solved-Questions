class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            found = False
            for i in range(num):
                if i | i+1 == num:
                    found = True
                    answer.append(i)
                    break
            if not found:
                answer.append(-1
                )
        return answer
    