class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        prev=[-1 for _ in range(m+1)] 
        for ind2 in range(m+1):
            prev[ind2]=0
        # for ind1 in range(n+1):
        #     dp[ind1][0]=0
        for ind1 in range(1,n+1):
            curr = [-1 for _ in range(m+1)]
            curr[0]=0
            for ind2 in range(1,m+1):
                if text1[ind1-1] == text2[ind2-1]:
                    curr[ind2] = 1 + prev[ind2-1] 
                else:
                    curr[ind2] =  0 + max(prev[ind2],curr[ind2-1])
            prev=curr
        return prev[m]
    def minInsertions(self, s: str) -> int:
        s1=s
        s2=s[::-1]
        a = self.longestCommonSubsequence(s1,s2)
        return len(s) - a