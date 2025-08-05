class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # If current value is within range, include it
        total = 0
        if low <= root.val <= high:
            total += root.val
        
        # Use BST property to optimize traversal
        if root.val > low:  # Only go left if we might find values >= low
            total += self.rangeSumBST(root.left, low, high)
        
        if root.val < high:  # Only go right if we might find values <= high
            total += self.rangeSumBST(root.right, low, high)
        
        return total
