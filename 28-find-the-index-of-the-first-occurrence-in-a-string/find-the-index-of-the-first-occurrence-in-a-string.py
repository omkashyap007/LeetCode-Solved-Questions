class Solution:
    def strStr(self, string : str, pattern : str) -> int:
        answer = []
        lps = [0 for _ in range(len(pattern))]
        prevLps = 0
        i = 1
        while i < len(pattern) :
            if pattern[i] == pattern[prevLps] : 
                prevLps += 1
                lps[i] = prevLps
                i += 1
            else :
                if prevLps == 0 : 
                    lps[i] = 0
                    i += 1
                else :
                    prevLps = lps[prevLps-1]
        i = j = 0
        while i < len(string) and j < len(pattern) :
            if string[i] == pattern[j] :
                i += 1
                j += 1
                if j == len(pattern) :
                    answer.append(i-j)
                    j = lps[j-1]
            else :
                if j == 0 :
                    i += 1
                else :
                    j = lps[j-1]
        if answer : 
            return answer[0]
        return -1