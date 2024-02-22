class Solution:

    def areAdjacent(self , first , second):
        i = j = count = 0
        while i < len(first) and j < len(second):
            if first[i] != second[j] :
                count += 1
                if count > 1 : return False
            i += 1
            j += 1
        return count == 1

    def createAdjacencyList(self , wordList):
        adj_list = {word:[] for word in wordList}
        for i in range(len(wordList)):
            for j in range(i+1 , len(wordList)):
                if self.areAdjacent(wordList[i] , wordList[j]) :
                    adj_list[wordList[i]].append(wordList[j]) 
                    adj_list[wordList[j]].append(wordList[i]) 
        return adj_list

    def udpateLevelDistance(self , levelDictionary , adj_list , beginWord , endWord):
        queue = deque([(beginWord , 1)])
        while queue : 
            root , level = queue.popleft()
            if root == endWord : 
                continue
            for node in adj_list[root] : 
                node_level = level + 1
                if node_level < levelDictionary[node] :
                    levelDictionary[node] = node_level
                    queue.append((node , node_level))

    def dfs(self , root , array , adj_list , levels  , answer):
        if levels[root] == float("inf") : 
            return 
        if levels[root] == 1 :
            answer.append(array.copy()[::-1])
            return
        for node in adj_list[root] : 
            if levels[node]== levels[root] - 1 : 
                array.append(node)
                self.dfs(node , array , adj_list , levels  , answer)
                array.pop()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        if beginWord not in wordList :
            wordList.append(beginWord)
        adj_list = self.createAdjacencyList(wordList)
        levelDistance = {word:float("inf") for word in wordList}
        levelDistance[beginWord] = 1
        self.udpateLevelDistance(levelDistance , adj_list , beginWord ,endWord)
        answer = []
        self.dfs(endWord , [endWord] , adj_list , levelDistance  , answer)
        return answer

