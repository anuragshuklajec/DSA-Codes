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
        rootNode.left =  self.buildTree(preorder[1:rootIndexInorder+1],inorder[:rootIndexInorder])
        rootNode.right = self.buildTree(preorder[rootIndexInorder+1:],inorder[rootIndexInorder + 1 :])

        return rootNode
    



        