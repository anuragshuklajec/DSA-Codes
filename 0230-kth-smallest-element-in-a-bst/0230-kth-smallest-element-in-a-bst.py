# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root,arr=[]):
            if not root:
                return arr
            dfs(root.left,arr)
            arr.append(root.val)
            dfs(root.right,arr)

            return arr 
        
        arr = dfs(root)
        return arr[k-1]
        
