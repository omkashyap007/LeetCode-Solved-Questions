class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num :
            while stack and stack[-1] > i and  k > 0 :
                stack.pop()
                k -= 1
            stack.append(i)
        while stack and k > 0 :
            stack.pop()
            k -=1 
        stack.reverse()
        while stack and stack[-1] == "0" :
            stack.pop()
            
        stack.reverse()
        if not stack : 
            return "0"
        return "".join(stack)