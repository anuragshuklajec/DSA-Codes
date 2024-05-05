# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node):
            if node is None:
                return True, 0
            isleftBal, left = checkBalance(node.left)
            isrightBal, right = checkBalance(node.right)
            if not isleftBal or not isrightBal or abs(left - right) > 1:
                return False, 1 + max(left,right)
            return True, 1 + max(left, right)

        isBalanced, height = checkBalance(root)
        return isBalanced