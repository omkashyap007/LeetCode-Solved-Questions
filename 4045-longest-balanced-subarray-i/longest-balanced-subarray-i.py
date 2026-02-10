class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            odd = {}
            even = {}
            for j in range(i, len(nums)):
                num = nums[j]
                if num % 2 == 0:
                    if num in even:
                        even[num] += 1
                    else:
                        even[num] = 1
                else:
                    if num in odd:
                        odd[num] += 1
                    else:
                        odd[num] = 1
                if len(even) == len(odd):
                    answer = max(answer, (j-i+1))
        return answer