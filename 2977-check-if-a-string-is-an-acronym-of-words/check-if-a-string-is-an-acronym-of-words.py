class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(list(map(lambda x : x[0] , words))) == s