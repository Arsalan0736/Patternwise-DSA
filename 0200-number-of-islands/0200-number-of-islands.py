class Solution:
    # def bfs(self,i,j,grid,vis):
    #     r=len(grid)
    #     c=len(grid[0])
    #     queue=deque()
    #     queue.append((i,j))
    #     while queue:
    #         x,y=queue.popleft()
    #         for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
    #             new_i,new_j=x+dx,y+dy
    #             if new_i<0 or new_i>=r or new_j<0 or new_j>=c:
    #                 continue
    #             if grid[new_i][new_j]=="0":
    #                 continue
    #             if vis[new_i][new_j]==1:
    #                 continue
    #             vis[new_i][new_j]=1
    #             queue.append((new_i,new_j))
    def dfs(self,i,j,grid,vis):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        if grid[i][j]=="0":
            return
        if vis[i][j]==1:
            return
        vis[i][j]=1
        self.dfs(i-1,j,grid,vis)
        self.dfs(i,j-1,grid,vis)
        self.dfs(i+1,j,grid,vis)
        self.dfs(i,j+1,grid,vis)
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0
        vis=[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and vis[r][c]==0:
                    count+=1
                    self.dfs(r,c,grid,vis)
        return count