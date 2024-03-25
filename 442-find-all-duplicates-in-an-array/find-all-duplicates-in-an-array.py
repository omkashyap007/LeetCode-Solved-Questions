class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = [0 for _ in range(len(nums))]
        for i in nums : 
            index = i-1
            if answer[index] == 0 :
                answer[index] = i
            else :
                answer[index]*=(-1)
        answer = [answer[i]*-1 for i in range(len(answer)) if answer[i] < 0 ]
        return answer