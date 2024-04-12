class Solution:

    def findOtherTwo(self , start , end , nums , target ,  answer) : 
        l = start 
        r = end 
        while l < r : 
            the_sum = nums[l] + nums[r] 
            if target == the_sum : 
                answer.append([-target , nums[l] , nums[r]])
                l += 1
                while l < r and nums[l-1] == nums[l] :
                    l += 1
            elif the_sum > target : 
                r -= 1
            else : 
                l += 1
        return 

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0 
        answer = []
        while i < len(nums) : 
            if i-1 >= 0 and nums[i] == nums[i-1] :
                i += 1
                continue
            target = -(nums[i])
            self.findOtherTwo(i+1 , len(nums)-1 , nums ,  target , answer)
            i += 1
        return answer