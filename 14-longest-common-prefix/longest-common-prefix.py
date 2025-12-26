class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        if len(strs) == 1:
            return strs[0]
        
        first_char = strs[0]
        for index, char in enumerate(first_char):
            found = True
            for word in strs[1:]:
                if len(word) <= index:
                    found = False
                    break
                if char != word[index]:
                    found = False
                    break
            if found:
                answer += char
            else:
                break
        return answer
