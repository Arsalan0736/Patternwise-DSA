class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        distance=[[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
                distance[i][i]=0
        for u,v,w in edges:
            distance[u][v]=w
            distance[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
        min_count=float("inf")
        ans=-1
        for i in range(n):
            count=0
            for j in range(n):
                if i!=j and distance[i][j]<=distanceThreshold:
                    count+=1
        
            if count<=min_count:
                min_count=count
                ans=i
        return ans