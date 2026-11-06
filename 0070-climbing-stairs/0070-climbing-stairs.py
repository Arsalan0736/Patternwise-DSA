class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        curr=0
        prev2=1
        prev=1
        for i in range(2,n+1):
            curr=prev2+prev
            prev2=prev
            prev=curr
        return prev