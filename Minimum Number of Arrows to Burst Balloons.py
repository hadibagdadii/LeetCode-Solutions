class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_position = points[0][1]
        
        for i in range(1, len(points)):
            start, end = points[i]
            
            if start > arrow_position:
                arrows += 1
                arrow_position = end
        
        return arrows
