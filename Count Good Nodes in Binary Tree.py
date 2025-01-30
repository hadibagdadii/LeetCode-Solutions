# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_so_far):
            if not node:
                return 0
                
            # Count current node if it's good
            count = 1 if node.val >= max_so_far else 0
            
            # Update max value seen on this path
            max_so_far = max(max_so_far, node.val)
            
            # Add counts from left and right subtrees
            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)
            
            return count
            
        return dfs(root, float('-inf'))
