class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        answer = 0
        for i in range(1 , len(prices)):
            answer = max(answer , prices[i] - min_value)
            min_value = min(min_value , prices[i])
        return answer