class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums :
            hash_map[i] = hash_map.get(i , 0)+1
        max_frequency = 0
        count = 0
        for i in hash_map :
            if hash_map[i] > max_frequency :
                max_frequency = hash_map[i]
                count = max_frequency
            elif hash_map[i] == max_frequency :
                count += max_frequency
        return count