class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        hash_set = set()
        for r in range(len(nums)):
            while abs(r-l) > k and l < r: 
                hash_set.discard(nums[l])
                l += 1
            if nums[r] in hash_set :
                return True
            hash_set.add(nums[r])
        return False