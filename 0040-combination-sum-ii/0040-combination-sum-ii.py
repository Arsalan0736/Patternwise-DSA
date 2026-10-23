class Solution:
    def solve(self,index,total,subset,nums,target,result):
        if total==target:
            result.append(subset.copy())
            return
        if total>target or index>=len(nums):
            return
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            self.solve(i+1,total+nums[i],subset,nums,target,result)
            subset.pop()
            # self.solve(i+1,total,subset,nums,target,result)

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        candidates.sort()
        self.solve(0,0,[],candidates,target,result)
        return result