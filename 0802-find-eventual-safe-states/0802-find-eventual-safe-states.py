class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V=len(graph)
        adj_list=[[] for _ in range(V)]
        outdegres=[0]*V
        queue=deque()
        safe=[]
        for u in range(V):
            for v in graph[u]:
                adj_list[v].append(u)
                outdegres[u]+=1
        for i in range(V):
            if outdegres[i]==0:
                queue.append(i)
                # adj_list.remove(i)
        while queue:
            curr_node=queue.popleft()
            safe.append(curr_node)
            for adjNode in adj_list[curr_node]:
                outdegres[adjNode]-=1
                if outdegres[adjNode]==0:
                    queue.append(adjNode)
        return sorted(safe)
