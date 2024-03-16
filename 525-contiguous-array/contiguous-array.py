class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {0:-1}
        count = 0
        answer = 0
        for index , i in enumerate(nums) :
            count += 1 if i == 1 else -1
            if count in hash_map :
                start_index = hash_map[count] +1
                last_index = index
                answer = max(last_index-start_index+1 , answer)
            else:
                hash_map[count] = index
        return answer