class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        my_Set=set()
        for i in range(len(nums)):
            my_Set.add(nums[i])       
        longest=0
        for num in my_Set:
            if num-1 not in my_Set:
                x=num
                count=1
                while x+1 in my_Set:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest