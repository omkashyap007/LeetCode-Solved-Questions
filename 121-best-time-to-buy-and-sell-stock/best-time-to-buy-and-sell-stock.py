class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_value = prices[0]
        for i in range(len(prices)):
            answer = max(answer, prices[i] - min_value)
            min_value = min(min_value, prices[i])
        return answer