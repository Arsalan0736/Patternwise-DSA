class Solution:
    def lowerBound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        lb = n
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            # For lower bound, look for the first element >= target
            if nums[mid] >= target:
                lb = mid
                high = mid - 1  # Look for a smaller index on the left
            else:
                low = mid + 1
                
        return lb

    def upperBound(self, nums: list[int], target: int) -> int:
        n = len(nums)
        ub = n
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            # For upper bound, look for the first element > target
            if nums[mid] > target:
                ub = mid
                high = mid - 1  # Look for a smaller index on the left
            else:
                low = mid + 1
                
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        
        # 1. Find the lower bound
        lb = self.lowerBound(nums, target)
        
        # If lower bound reaches the end, or the element at lb is not the target,
        # it means the target does not exist in the array.
        if lb == n or nums[lb] != target:
            return [-1, -1]
            
        # 2. Find the upper bound
        ub = self.upperBound(nums, target)
        
        # The last position is always exactly one index before the upper bound
        return [lb, ub - 1]
