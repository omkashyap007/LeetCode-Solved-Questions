class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque([i for i in range(len(deck))])
        deck.sort()
        result = [0 for _ in range(len(deck))]
        for i in range(len(deck)):
            index = queue.popleft()
            result[index] = deck[i]
            if queue :
                queue.append(queue.popleft())
        return result

        answer = [0 for _ in range(len(deck))]
        deck.sort()
        skip = False
        i = j = 0
        while i < len(deck) :
            if answer[j] == 0 :
                if not skip :
                    answer[j] = deck[i]
                    i += 1
                skip = not skip
            j = (j+1)%len(deck)
        return answer