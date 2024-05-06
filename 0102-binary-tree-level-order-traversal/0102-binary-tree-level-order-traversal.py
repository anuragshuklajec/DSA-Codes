# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        curr = root
        temp = [[curr]] if curr is not None else []
        while temp:
            parents = temp.pop(0)
            res.append([parent.val for parent in parents if parent is not None])
            childrens= []
            for parent in parents:
                if parent and parent.left:
                    childrens.append(parent.left)
                if parent and parent.right:
                    childrens.append(parent.right)
            if childrens:
                temp.append(childrens)
        return res
            

            
        