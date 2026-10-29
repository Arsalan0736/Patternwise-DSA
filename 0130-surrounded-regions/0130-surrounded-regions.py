class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    board[r][c]='S'
                    queue.append((r,c))
        while queue:
            i,j=queue.popleft()
            for x,y in[(-1,0),(0,-1),(1,0),(0,1)]:
                new_i,new_j=i+x,j+y
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if board[new_i][new_j] == 'O':
                    board[new_i][new_j]='S'
                    queue.append((new_i,new_j))
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='S':
                    board[r][c]='O'
        return board
