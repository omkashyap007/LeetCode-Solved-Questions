class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        start = []
        end = []
        for index , i in enumerate(s) : 
            if i == "(" :
                start.append(("(" , index))
            if i == ")" :
                if start :
                    start.pop()
                else :
                    end.append((")" , index))
        s = list(s)
        j = k = 0 
        for i in range(len(s)):
            if s[i] == "(" :
                if start and  j < len(start) and start[j][1] == i : 
                    s[i] = ""
                    j += 1
            if s[i] == ")" :
                if end and k < len(end) and end[k][1] == i :
                    s[i] = ""
                    k += 1
        return "".join(s)