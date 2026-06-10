# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans=0
        def depth(root:Optional[TreeNode],temp: int):
            nonlocal ans
            if root==None:
                ans=max(temp,ans)
                return
            depth(root.left,temp+1)
            depth(root.right,temp+1)
            return
        depth(root,0)

        return ans
            

            

        