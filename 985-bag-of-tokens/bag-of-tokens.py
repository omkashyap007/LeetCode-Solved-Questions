class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        max_score = 0
        score = 0
        l , r = 0 , len(tokens)-1
        while l <= r :
            if power >= tokens[l] :
                power -= tokens[l]
                score += 1
                max_score = max(score , max_score)
                l += 1
            elif score >= 1:
                power += tokens[r]
                score -= 1
                r -= 1
            else :
                break
        return max_score