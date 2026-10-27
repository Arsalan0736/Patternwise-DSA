# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def solve(node):
            if node == None:
                return 0
            LH=solve(node.left)
            if LH==-1:
                return -1
            RH=solve(node.right)
            if RH==-1:
                return -1
            if abs(RH-LH)>1:
                return -1
            return 1+max(LH,RH)
        return solve(root)!=-1