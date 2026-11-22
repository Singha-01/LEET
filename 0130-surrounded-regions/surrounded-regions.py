class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark cell as connected to border
            board[r][c] = 'E'
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Run DFS for all 'O's on the outer boundaries
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == 'O':
                    dfs(r, c)

        # Step 2: Update the board in-place
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'   # Captured region
                elif board[r][c] == 'E':
                    board[r][c] = 'O'   # Restored region