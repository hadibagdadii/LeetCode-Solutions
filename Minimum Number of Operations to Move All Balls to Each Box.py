class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        balls_left = 0
        operations_left = 0
        
        for i in range(n):
            result[i] = operations_left
            balls_left += int(boxes[i])
            operations_left += balls_left
        
        balls_right = 0
        operations_right = 0
        
        for i in range(n - 1, -1, -1):
            result[i] += operations_right
            balls_right += int(boxes[i])
            operations_right += balls_right
            
        return result
