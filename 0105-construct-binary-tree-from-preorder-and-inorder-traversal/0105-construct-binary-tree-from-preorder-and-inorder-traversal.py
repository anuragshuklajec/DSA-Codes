# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        rootNode = TreeNode(preorder[0])
        rootIndexInorder = inorder.index(preorder[0])
        leftinorder = inorder[:rootIndexInorder]
        rightinorder = inorder[rootIndexInorder + 1 :]

        lengthLeftInorder = len(leftinorder)

        leftpreorder = preorder[1:lengthLeftInorder+1]
        rightpreorder = preorder[lengthLeftInorder+1:]

        rootNode.left =  self.buildTree(leftpreorder,leftinorder)
        rootNode.right = self.buildTree(rightpreorder,rightinorder)

        return rootNode
    



        