class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res=[0]*len(nums)
        posIdx,negIdx=0,1
        for i in range(len(nums)):
            if nums[i]>=0:
                res[posIdx]=nums[i]
                posIdx+=2
            else:
                res[negIdx]=nums[i]
                negIdx+=2
        return res