class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hash_map = {}
        for i in nums :
            hash_map[i] = hash_map.get(i , 0)+1
        answer = 0
        left = 0
        count_map = {}
        req = len(hash_map)
        have = 0
        for r in range(len(nums)) :
            count_map[nums[r]] = count_map.get(nums[r],0)+1
            while count_map[nums[r]] > k and left <= r :
                count_map[nums[left]] -=1 
                if count_map[nums[left]] == 0 :
                    del count_map[nums[left]]
                left += 1
            answer = max(r-left+1 , answer)
        return answer