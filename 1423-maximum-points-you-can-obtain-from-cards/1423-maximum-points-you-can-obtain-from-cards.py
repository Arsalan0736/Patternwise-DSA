class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        left,right,right_ind,maxi=0,0,n-1,0
        for i in range(k):
            left+=cardPoints[i]
        maxi=left
        for i in range(k-1,-1,-1):
            left-=cardPoints[i]
            right+=cardPoints[right_ind]
            right_ind-=1
            maxi=max(maxi,left+right)
        return maxi