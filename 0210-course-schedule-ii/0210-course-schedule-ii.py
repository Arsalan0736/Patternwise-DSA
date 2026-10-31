class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list=[[] for _ in range(numCourses)]
        indegres=[0]*numCourses
        queue=deque()
        result=[]
        for u,v in prerequisites:
            adj_list[v].append(u)
            indegres[u]+=1
        for i in range(numCourses):
            if indegres[i]==0:
                queue.append(i)
        while queue:
            curr_node=queue.popleft()
            result.append(curr_node)
            for adjNode in adj_list[curr_node]:
                indegres[adjNode]-=1
                if indegres[adjNode]==0:
                    queue.append(adjNode)
        if len(result)==numCourses:
            return result
        return []