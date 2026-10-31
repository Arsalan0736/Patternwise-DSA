class Solution:
    def dfs(self,curr_idx,graph,vis,color):
        vis[curr_idx]=color
        for adjNode in graph[curr_idx]:
            if vis[adjNode]!=-1:
                if vis[adjNode]==color:
                    return False
            else:
                if self.dfs(adjNode,graph,vis,1-color) == False:
                    return False
        return True
    def isBipartite(self, graph: list[list[int]]) -> bool:
        total_nodes=len(graph)
        vis=[-1]*total_nodes
        for index in range(total_nodes):
            if vis[index]==-1:
                if self.dfs(index,graph,vis,0) == False:
                    return False
        return True