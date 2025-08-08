class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Find the maximum value and its index
        max_val = max(nums)
        max_idx = nums.index(max_val)
        
        # Create root node with maximum value
        root = TreeNode(max_val)
        
        # Recursively build left and right subtrees
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
        
        return root
