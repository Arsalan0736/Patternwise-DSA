class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n=len(g)
        m=len(s)
        count,i,j=0,0,0
        g.sort()
        s.sort()
        while i<n and j<m:
            if s[j]>=g[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count