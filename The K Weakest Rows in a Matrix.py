class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Count soldiers in each row and pair with row index
        strength = []
        for i in range(len(mat)):
            soldier_count = sum(mat[i])  # Count 1s in the row
            strength.append((soldier_count, i))
        
        # Sort by soldier count, then by row index
        strength.sort()
        
        # Return first k row indices
        return [row_idx for soldier_count, row_idx in strength[:k]]
