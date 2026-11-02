class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        r=len(heights)
        c=len(heights[0])
        effort=[[sys.maxsize for _ in range(len(heights[0]))] for _ in range(len(heights))]
        effort[0][0]=0
        priority_queue=[]
        priority_queue.append([0,0,0])

        while priority_queue:
            eff,i,j=heapq.heappop(priority_queue)
            if i==r-1 and j==c-1:
                return eff

            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i,new_j=i+x,j+y
                if new_i<0 or new_i>=r or new_j<0 or new_j>=c:
                    continue
                curr_eff=abs(heights[new_i][new_j]-heights[i][j])
                max_eff=max(eff,curr_eff)

                if max_eff < effort[new_i][new_j]:
                    effort[new_i][new_j]=max_eff
                    heapq.heappush(priority_queue,[max_eff,new_i,new_j])
