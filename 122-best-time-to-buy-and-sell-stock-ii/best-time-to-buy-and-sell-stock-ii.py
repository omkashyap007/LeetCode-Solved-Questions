class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        stack = []
        for i in prices:
            if stack and stack[-1] > i:
                stack.pop()
            elif stack and stack[-1] < i:
                answer += (i-stack[-1])
                stack.pop()
            stack.append(i)
        return answer