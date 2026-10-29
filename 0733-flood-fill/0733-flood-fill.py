class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc]==color:
            return image
        vis=deepcopy(image)
        rows=len(vis)
        cols=len(vis[0])
        initial_color=vis[sr][sc]
        queue=deque()
        queue.append((sr,sc))
        vis[sr][sc]=color
        while len(queue)!=0:
            i,j=queue.popleft()
            vis[i][j]=color
            for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_i=i+x
                new_j=j+y
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue
                if vis[new_i][new_j]!=initial_color:
                    continue
                queue.append((new_i,new_j))
                vis[new_i][new_j] = color
        return vis

                