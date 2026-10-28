# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxSum=float("-inf")
        def solve(node):
            nonlocal maxSum
            if node is None:
                return 0
            leftSum=solve(node.left)
            if leftSum<0:
                leftSum=0
            rightSum=solve(node.right)
            if rightSum<0:
                rightSum=0
            maxSum=max(maxSum,leftSum+node.val+rightSum)
            return node.val+max(leftSum,rightSum)
        solve(root)
        return maxSum