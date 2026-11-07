class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        m=len(grid)
        n=len(grid[0])
        prev=[-1]*n
        for i in range(m):
            curr=[-1]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[0]=grid[0][0]
                    continue
                if i==0:
                    up=float("inf")
                else:
                    up=prev[j]
                if j==0:
                    left=float("inf")
                else:
                    left=curr[j-1]
                curr[j]=grid[i][j]+min(up,left)
            prev=curr
        return prev[n-1]
                