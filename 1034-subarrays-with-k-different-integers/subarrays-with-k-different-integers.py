class Solution:

    def atLeastK(self , nums , k):
        answer = 0
        left = 0
        count_map = {}
        for r in range(len(nums)) :
            count_map[nums[r]] = count_map.get(nums[r],0)+1
            while len(count_map) > k :
                count_map[nums[left]] -=1 
                if count_map[nums[left]] == 0 :
                    del count_map[nums[left]]
                left += 1
            answer += r-left+1
        return answer

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atLeastK(nums ,  k) - self.atLeastK(nums , k-1)