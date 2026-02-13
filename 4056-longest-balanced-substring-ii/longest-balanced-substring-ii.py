class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        res = 0
        count = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        
        aPre = []
        bPre = []
        cPre = []
        aCount = 0
        bCount = 0
        cCount = 0
        for c in s:
            if c == 'a':
                aCount += 1
            elif c == 'b':
                bCount += 1
            else:
                cCount += 1
            aPre.append(aCount)
            bPre.append(bCount)
            cPre.append(cCount)
        
        def case2(pre1, pre2, pre3):
            case2Max = 0
            diffMap = {0: -1}
            lastPre3 = 0

            for j in range(n):
                if pre3[j] > lastPre3:
                    diffMap = {pre1[j] - pre2[j]: j}
                    lastPre3 = pre3[j]
                    continue
                
                diff = pre1[j] - pre2[j]
                
                if diff in diffMap:
                    idx = diffMap[diff]
                    case2Max = max(case2Max, j - idx)
                else:
                    diffMap[diff] = j
            
            return case2Max
        
        res = max(res, max(case2(aPre, bPre, cPre), case2(aPre, cPre, bPre), case2(bPre, cPre, aPre)))

        case3Hash = {(0, 0): -1}
        for k in range(n):
            val = (aPre[k] - bPre[k], aPre[k] - cPre[k])
            
            if val in case3Hash:
                idx = case3Hash[val]
                res = max(res, k - idx)
            else:
                case3Hash[val] = k

        return res