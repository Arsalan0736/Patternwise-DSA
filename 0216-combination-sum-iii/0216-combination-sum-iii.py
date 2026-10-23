class Solution:
    def solve(self,index,subset,total,k,n,result):
        if total>=n:
            if total==n and len(subset)==k:
                result.append(subset.copy())
            return
        if len(subset)>k:
            return
        for i in range(index,10):
            subset.append(i)
            self.solve(i+1,subset,total+i,k,n,result)
            subset.pop()
            
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        self.solve(1,[],0,k,n,result)
        return result