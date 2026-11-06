class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[-1]*n
        for i in range(0,m):
            curr=[-1]*n
            for j in range(0,n):
                if i==0 and j==0:
                    curr[0]=1
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