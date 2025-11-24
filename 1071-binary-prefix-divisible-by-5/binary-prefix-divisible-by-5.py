class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        answer = []
        for i in nums:
            num = num*2 + i
            answer.append(num%5 == 0)
        return answer
                
            