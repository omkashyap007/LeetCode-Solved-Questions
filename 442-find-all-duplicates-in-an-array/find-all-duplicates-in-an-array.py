class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)): 
            item = abs(nums[i])
            if nums[item-1] < 0 : 
                answer.append(abs(nums[i]))
            else :
                nums[item-1] *= (-1)
        return answer