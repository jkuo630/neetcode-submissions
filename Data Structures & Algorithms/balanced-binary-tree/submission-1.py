# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # maxheight of left 
        # maxheight of right 
        # check if they are no more than 1 
        if not root:
            return True

        def maxHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0 
            return 1 + max(maxHeight(root.left), maxHeight(root.right))
        
        left = maxHeight(root.left)
        right = maxHeight(root.right)

        return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)