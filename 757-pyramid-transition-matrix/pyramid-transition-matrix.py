class Solution:

    def check(self, i, bl, nl, hash_map):
        # print(i, bl, nl)
        if len(bl) == 1:
            return True
        
        for j in range(i, len(bl)-1):
            c = bl[i]+bl[i+1]
            if c not in hash_map or not hash_map[c]:
                return False
            for t in hash_map[c]:
                nl.append(t)
                f = self.check(j+1, bl, nl, hash_map)
                if f:
                    return True
                nl.pop()
        if len(nl) == len(bl)-1:
            return self.check(0, nl, [], hash_map)
        return False


    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        b = list(bottom)
        allowed_map = {}
        for string in allowed:
            allowed_map[string[:2]] = allowed_map.get(string[:2], []) + [string[2:]]
        # print(b)
        return self.check(0, b, [], allowed_map)