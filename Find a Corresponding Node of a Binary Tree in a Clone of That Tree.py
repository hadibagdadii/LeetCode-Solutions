class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def pre(orig_node, clone_node):
            if not orig_node:
                return None
            
            if orig_node == target:
                return clone_node

            left_result = pre(orig_node.left, clone_node.left)
            if left_result:
                return left_result

            return pre(orig_node.right, clone_node.right)
        
        return pre(original, cloned)
