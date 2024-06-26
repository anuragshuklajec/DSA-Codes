# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        res = [-1001]
        def dfs(root):
            if root == None:
                return 0
            leftMax = dfs(root.left)
            leftMax =  max(leftMax,0)
            rightMax = dfs(root.right)
            rightMax = max(rightMax,0)
            res[0] = max(res[0],root.val + leftMax + rightMax )
            return root.val + max(leftMax,rightMax)
        dfs(root)
        return res[0]