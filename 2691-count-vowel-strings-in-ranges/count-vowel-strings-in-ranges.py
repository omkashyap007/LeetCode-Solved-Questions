class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        l = [0 for _ in range(len(words))]
        for index, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                l[index] = l[index-1 if index > 0 else 0] + 1
            else:
                l[index] = l[index-1 if index > 0 else index]
        print(l)
        answer = []
        for start, end in queries:
            if start == 0:
                answer.append(l[end])
            else:
                answer.append(l[end] - l[start-1])
        return answer
