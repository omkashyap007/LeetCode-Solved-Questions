class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def total_area(mid_y):
            area_above, area_below = 0, 0
            for square in squares:
                bottom_x, bottom_y, side = square

                top_y = bottom_y + side
                
                # CASE 1: Square COMPLETELY ABOVE line (bottom_y > mid_y)
                # Intuition: Entire square contributes to top area
                if bottom_y > mid_y:
                    area_above += (side * side)
                    continue
                
                # CASE 2: Square COMPLETELY BELOW line (top_y < mid_y)  
                # Intuition: Entire square contributes to bottom area
                if top_y < mid_y:
                    area_below += (side * side)
                    continue
                
                # CASE 3: Line CUTS THROUGH square (bottom_y ≤ mid_y ≤ top_y)
                # Intuition: Split square into 2 rectangles at mid_y
                # Top rectangle height = (top_y - mid_y), width = side
                # Bottom rectangle height = (mid_y - bottom_y), width = side
                area_above += ((top_y - mid_y) * side)
                area_below += ((mid_y - bottom_y) * side)
                
            return area_above, area_below
        
        # Find exact y-range containing ALL squares
        l, r = float('inf'), float('-inf')
        for square in squares:
            bottom_x, bottom_y, side = square
            l = min(l, bottom_y)
            r = max(r, bottom_y + side)

        ans = -1    # Track BEST (lowest) candidate y

        while r - l > 0.00001:  # Stop when precise enough (1e-5 accuracy)
            mid = (l + r)/2.0

            area_above, area_below = total_area(mid)

            # DECISION LOGIC - Purely geometric intuition:
            # if, top_area > bottom_area → too much area above line
            # Solution must exist HIGHER UP → search [mid, r]
            # else, top_area ≤ bottom_area → valid 
            # Try LOWER position to minimize y → search [l, mid]
            if area_above > area_below:
                l = mid
            else:
                r = mid
                ans = mid
        
        return ans