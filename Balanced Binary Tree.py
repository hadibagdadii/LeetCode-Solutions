class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            # Base case: empty node has height 0
            if not node:
                return 0
            
            # Get height of left subtree
            left_height = check_height(node.left)
            if left_height == -1:  # Left subtree is unbalanced
                return -1
            
            # Get height of right subtree
            right_height = check_height(node.right)
            if right_height == -1:  # Right subtree is unbalanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Signal unbalanced
            
            # Return height of current subtree
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1
