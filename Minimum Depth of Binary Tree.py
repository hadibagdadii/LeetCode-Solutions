class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If it's a leaf node
        if not root.left and not root.right:
            return 1
        
        # If only one child exists, go down that path
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both children exist, take minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
