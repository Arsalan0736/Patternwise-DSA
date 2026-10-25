class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(0,n):
            seen=set()
            for j in range(i,n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    ans=max(ans,j-i+1)
        return ans