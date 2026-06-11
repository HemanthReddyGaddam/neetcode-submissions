# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def level(
        self,
        root: Optional[TreeNode],
        mp: Dict[int, List[int]],
        count: int
    ) -> None:
        if not root:
            return

        if count not in mp:
            mp[count] = []

        mp[count].append(root.val)

        self.level(root.left, mp, count + 1)
        self.level(root.right, mp, count + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp: Dict[int, List[int]] = {}
        self.level(root, mp, 0)

        return [mp[i] for i in range(len(mp))]

        