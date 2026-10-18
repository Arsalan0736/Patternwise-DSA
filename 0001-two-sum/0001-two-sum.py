class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        hash_map={}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining],i]
            hash_map[nums[i]]=i