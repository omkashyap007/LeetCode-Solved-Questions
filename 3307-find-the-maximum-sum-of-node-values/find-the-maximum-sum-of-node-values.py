class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sum_val = 0
        cnt = 0
        sacrifice = float('inf')
        for n in nums:
            sum_val += max(n ^ k, n)
            cnt += (n ^ k) > n
            sacrifice = min(sacrifice, abs(n - (n ^ k)))
        
        return sum_val - (sacrifice if cnt % 2 else 0)