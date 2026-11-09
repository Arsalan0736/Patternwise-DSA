class Solution:
    def solve(self,ind1,ind2,text1,text2,dp):
        if ind1 == 0 or ind2 == 0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if text1[ind1-1] == text2[ind2-1]:
            dp[ind1][ind2] = 1 + self.solve(ind1-1,ind2-1,text1,text2,dp)
            return dp[ind1][ind2]
        dp[ind1][ind2] =  0 + max(self.solve(ind1-1,ind2,text1,text2,dp), self.solve(ind1,ind2-1,text1,text2,dp))
        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
        return self.solve(n,m,text1,text2,dp)