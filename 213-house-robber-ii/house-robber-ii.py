class Solution:

    def dfs(self , index , taken , cache , nums):
        if (index,taken)  in cache :
            return cache[(index,taken)]
        if index == 0 and taken : 
            return 0
        if index == 0 and  not taken : 
            return nums[0]
        if index == 1 and taken :
            return nums[1]
        if index == 1 and not taken : 
            return max(nums[0] , nums[1])
        prev_step = self.dfs(index-1 , taken , cache , nums)
        curr_step = self.dfs(index-2 , taken , cache ,  nums) + nums[index]
        cache[(index,taken)] = max(prev_step , curr_step)
        return cache[(index,taken)]
        

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        cache = {}
        answer = max(
                self.dfs(len(nums)-2 , False, cache , nums) , 
                self.dfs(len(nums)-1 , True , cache , nums)
            )
        return answer