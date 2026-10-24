class Solution:
    def solve(self,col,ans,board,leftRow,lowerDiagonal,upperDiagonal,n):
        if col==n:
            ans.append(board[:])
            return
        for row in range(n):
            if ( leftRow[row]==0 and lowerDiagonal[col+row]==0 and upperDiagonal[n-1+col-row]==0):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                leftRow[row]=1
                lowerDiagonal[col+row]=1
                upperDiagonal[n-1+col-row]=1
                self.solve(col+1,ans,board,leftRow,lowerDiagonal,upperDiagonal,n)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                leftRow[row]=0
                lowerDiagonal[col+row]=0
                upperDiagonal[n-1+col-row]=0


    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        board=["."*n for _ in range(n)]
        leftRow=[0]*n
        lowerDiagonal=[0]*n*(2*n-1)
        upperDiagonal=[0]*n*(2*n-1)
        self.solve(0,ans,board,leftRow,lowerDiagonal,upperDiagonal,n)
        return ans