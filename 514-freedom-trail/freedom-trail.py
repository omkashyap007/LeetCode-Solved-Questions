class Solution:

    @cache
    def dfs(self , key_index , ring_index , rotate_count , direction , key , ring ) :
        if key[key_index] == ring[ring_index] :
            if key_index == len(key)-1 :
                return 0
            forward_ring_index = 0 if ring_index == len(ring)-1 else ring_index+1
            backward_ring_index = len(ring)-1 if ring_index == 0 else ring_index-1
            forward_side = 1+self.dfs(key_index +1 , forward_ring_index , 0 , 1 , key , ring )
            backward_side = 1+self.dfs(key_index +1  , backward_ring_index , 0 , -1 , key , ring )
            curr = self.dfs(key_index+1 , ring_index , 0 , 1 , key , ring )
            return 1+min([ forward_side , backward_side , curr ])
        else :
            if direction == 1 :
                forward_ring_index = 0 if ring_index == len(ring)-1 else ring_index+1
                return 1+self.dfs(key_index , forward_ring_index , rotate_count +1  , direction , key , ring )
            else :
                backward_ring_index = len(ring)-1 if ring_index == 0 else ring_index-1
                return 1+self.dfs(key_index , backward_ring_index , rotate_count +1  , direction , key , ring)


    def findRotateSteps(self, ring: str, key: str) -> int:
        if ring[0] == key[0] : 
            return 1+self.dfs(0 , 0 , 0 , -1 , key , ring )
        else :
            return 1+min(
                self.dfs(0 , 0 , 0 , -1 , key , ring ) ,
                self.dfs(0 , 0 , 0 , 1 , key , ring )
            )