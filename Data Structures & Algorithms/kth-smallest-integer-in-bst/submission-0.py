# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal 
        # keep a counter, once its at k, return that node 
        self.counter = 0
        self.ans = None
        def dfs(node: Optional[TreeNode]) -> int:
            if not node or self.ans is not None:
                return 
            if node.left:
                dfs(node.left)
            self.counter += 1
            if self.counter == k:
                self.ans = node.val
                return 
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return self.ans
