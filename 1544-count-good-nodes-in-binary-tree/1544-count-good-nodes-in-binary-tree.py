# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxEle):
            if root == None:
                return 0
            if root.val >= maxEle:
                maxEle = root.val
                return 1 + dfs(root.left,maxEle) + dfs(root.right,maxEle)
            else:
                return dfs(root.left,maxEle) + dfs(root.right,maxEle)

        return dfs(root,-10001)
        
        