class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list=[[] for _ in range(numCourses)]
        indegres=[0]*numCourses
        queue=deque()
        result=[]
        for u,v in prerequisites:
            adj_list[u].append(v)
            indegres[v]+=1
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
            return True
        return False
        