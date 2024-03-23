class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]" :
                string = ""
                while stack and stack[-1] != "[" :
                    string = stack.pop() + string
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit() :
                    digit = stack.pop() + digit
                stack.append(int(digit)*string)
            else :
                stack.append(s[i])
        return "".join(stack)