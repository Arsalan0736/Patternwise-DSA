class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        prev=[-1]*n
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            curr=[-1]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[0]=1
                    continue
                if obstacleGrid[i][j]==1:
                    curr[j]=0
                    continue
                if i==0:
                    up=0
                else:
                    up=prev[j]
                if j==0:
                    left=0
                else:
                    left=curr[j-1]
                curr[j]=up+left
            prev=curr
        return prev[n-1]
                