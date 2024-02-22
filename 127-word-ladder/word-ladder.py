class Solution:

    def areAdjacent(self , first , second):
        i = j = count = 0 
        while i < len(first) and j < len(second) :
            if first[i] != second[j] :
                count += 1
                if count > 1 :
                    return False
            i += 1
            j += 1
        return count == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList :
            return 0
        if beginWord not in wordList :
            wordList.append(beginWord)
        adj_list = {word:[] for word in wordList}
        for i in range(len(wordList)):
            for j in range(i+1 ,len(wordList)):
                if i == j : continue
                if self.areAdjacent(wordList[i] , wordList[j]) : 
                    adj_list[wordList[i]].append(wordList[j])
                    adj_list[wordList[j]].append(wordList[i])
        queue = deque([(1 , beginWord)])
        distances = {word : float("inf") for word in wordList}
        min_distance = float("inf")
        while queue : 
            distance , root = queue.popleft()
            if root == endWord :
                min_distance = min(min_distance , distance)
                continue
            for node in adj_list[root] :
                node_distance = distance + 1
                if node_distance < distances[node] : 
                    distances[node] = node_distance
                    queue.append((node_distance , node))
        return 0 if min_distance == float("inf") else min_distance