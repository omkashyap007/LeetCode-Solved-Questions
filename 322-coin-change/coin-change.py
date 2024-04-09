class Solution:

    def dfs(self , index , coins , amount , cache) :
        if index == 0 :
            if amount%coins[index] == 0:
                return amount//coins[index]
            return float("inf")
        if (index, amount) in cache :
            return cache[(index,amount)]
        not_take = self.dfs(index-1 , coins , amount , cache)
        take = float("inf")
        if coins[index] <= amount : 
            take = 1 + self.dfs(index , coins , amount-coins[index] , cache)
        cache[(index,amount)] = min(take, not_take)
        return min(take , not_take)

    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        value = self.dfs(len(coins)-1 , coins ,amount , cache)
        if value == float("inf") : return -1
        return value