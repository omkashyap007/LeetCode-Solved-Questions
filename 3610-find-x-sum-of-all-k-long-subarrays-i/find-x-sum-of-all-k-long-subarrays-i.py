class Solution:

    def mostFrequent(self, array, x):
        hash_map = {}
        for i in array:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        l = []
        for i in hash_map:
            l.append((hash_map[i], i))
        l.sort(key = lambda x: (x[0], x[1]), reverse=True)
        a = l[:x]
        return sum([count*item for count, item in a])

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        for i in range(n-k+1):
            subarray = nums[i:i+k]
            answer.append(self.mostFrequent(subarray, x))
        return answer
