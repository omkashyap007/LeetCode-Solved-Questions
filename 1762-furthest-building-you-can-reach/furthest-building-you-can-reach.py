class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        bricks_heap = []
        for i in range(len(heights)-1):
            if heights[i] >= heights[i+1] :
                continue
            bricks_required = heights[i+1]-heights[i]
            bricks -= bricks_required
            heapq.heappush(bricks_heap , - bricks_required)
            if bricks < 0 :
                ladders -= 1
                bricks += -heapq.heappop(bricks_heap)
            if ladders <0 :
                return i
        return len(heights)-1