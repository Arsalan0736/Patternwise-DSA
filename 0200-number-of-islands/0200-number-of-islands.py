class Solution:
    def bfs(self,i,j,vis,grid):
        r=len(grid)
        c=len(grid[0])
        queue=deque()
        queue.append((i,j))
        vis[i][j]=1
        while queue:
            x,y=queue.popleft()
            for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
                new_i,new_j=x+dx,y+dy
                if new_i<0 or new_i>=r or new_j<0 or new_j>=c:
                    continue
                if grid[new_i][new_j]=="0":
                    continue
                if vis[new_i][new_j]==1:
                    continue
                vis[new_i][new_j]=1
                queue.append((new_i,new_j))

    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        vis=[[0 for _ in range(cols)] for _ in range(rows)]
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and vis[r][c]==0:
                    count+=1
                    self.bfs(r,c,vis,grid)
        
        return count
                