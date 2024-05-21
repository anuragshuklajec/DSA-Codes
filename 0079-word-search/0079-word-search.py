class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROWS,COLS = len(board),len(board[0])
        def dfs(r,c,i):
            if i == len(word):
                return word
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path:
                return False
            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return res
        
        for R in range(ROWS):
            for C in range(COLS):
                if dfs(R,C,0): return True
        return False

        