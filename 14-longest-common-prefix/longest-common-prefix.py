class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        if not strs:
            return answer
        first = strs[0]
        for i in range(len(first)):
            for j in range(1, len(strs)):
                if len(strs[j])-1 < i:
                    return answer
                if first[i] != strs[j][i]:
                    return answer
            answer += first[i]
        return answer
