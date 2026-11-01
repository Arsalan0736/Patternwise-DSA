class Solution:
    def dfs(self,curr_node,graph,vis,path_vis,safe):
        vis[curr_node]=1
        path_vis[curr_node]=1
        for adjNode in graph[curr_node]:
            if vis[adjNode]==0:
                ans = self.dfs(adjNode,graph,vis,path_vis,safe)
                if ans == False:
                    return False
            elif path_vis[adjNode]==1:
                return False
        safe[curr_node]=1
        path_vis[curr_node]=0
        return True

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V=len(graph)
        vis=[0 for _ in range(V)]
        path_vis=[0 for _ in range(V)]
        safe=[0 for _ in range(V)]
        for i in range(V):
            if vis[i]==0:
                self.dfs(i,graph,vis,path_vis,safe)
        res=[]
        for i in range(V):
            if safe[i]==1:
                res.append(i)
        return res