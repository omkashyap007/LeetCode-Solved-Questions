class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0: 
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k > 0 and stack :
            stack.pop()
            k -= 1
        stack.reverse()
        while stack and stack[-1] == "0" :
            stack.pop()
        stack.reverse()
        value = "".join(stack)
        return "0" if not value else "".join(stack)