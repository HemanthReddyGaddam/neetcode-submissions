# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode],ans:List[int]):
        if root==None:
            return 
        self.inorder(root.left,ans)
        ans.append(root.val)
        self.inorder(root.right,ans)
        return 

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.inorder(root,ans)
        return ans
        