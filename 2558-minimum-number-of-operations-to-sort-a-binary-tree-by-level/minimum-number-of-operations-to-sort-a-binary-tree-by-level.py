class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = []
        answer = 0
        queue = [root]
        while queue : 
            l = []
            q = []
            for node in queue :
                l.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            if l :
                levels.append(l)
            queue = q
        if len(levels) == 1 :
            return 0
        for i in range(1 ,len(levels)):
            level = levels[i]
            level_hash_map = {level[j] : j for j in range(len(level))}
            sorted_level = sorted(level)
            for j in range(len(level)):
                if sorted_level[j] == level[j] :
                    continue
                a = level[j]
                a_index = level_hash_map[a]
                b = sorted_level[j]
                b_index = level_hash_map[b]
                level[a_index] , level[b_index] = level[b_index] , level[a_index]
                level_hash_map[a] = b_index
                level_hash_map[b] = a_index
                answer += 1
        return answer