# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = []
        if root is None:
            return []
        q.append(root)
        while q:
            lenQ = len(q)
            found = False
            for _ in range(lenQ):
                curr = q.pop(0)
                found = True
                lastNum = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if found:
                res.append(lastNum)
        return res


        