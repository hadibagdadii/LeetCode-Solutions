class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(numRows):
            row = [1] * (i + 1)  # Create row with all 1s
            
            # Fill in the middle values
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            
            result.append(row)
        
        return result
