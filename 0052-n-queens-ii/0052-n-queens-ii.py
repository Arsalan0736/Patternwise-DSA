class Solution:
    def solve(self,col,count,leftRow,lowerDiagonal,upperDiagonal,n):
        if col==n:
            count[0]+=1
            return
        for row in range(n):
            if (leftRow[row]==0 and lowerDiagonal[row+col]==0 and upperDiagonal[n-1+col-row]==0):
                leftRow[row]=1
                lowerDiagonal[row+col]=1
                upperDiagonal[n-1+col-row]=1
                self.solve(col+1,count,leftRow,lowerDiagonal,upperDiagonal,n)
                leftRow[row]=0
                lowerDiagonal[row+col]=0
                upperDiagonal[n-1+col-row]=0
    def totalNQueens(self, n: int) -> int:
        count=[0]
        leftRow=[0]*n
        lowerDiagonal=[0]*(2*n-1)
        upperDiagonal=[0]*(2*n-1)
        self.solve(0,count,leftRow,lowerDiagonal,upperDiagonal,n)
        return count[0]