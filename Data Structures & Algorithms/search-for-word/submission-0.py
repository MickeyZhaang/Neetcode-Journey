class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def inBounds(row, col):
            return row >= 0 and col >= 0 and row < len(board) and col < len(board[row])

        for i, r in enumerate(board):
            for j, c in enumerate(board[i]):
                q = [(i, j)]
                ctr = 0
                while q:
                    if ctr == len(word):
                        return True
                    row, col = q.pop(0)
                    if not inBounds(row, col):
                        continue
                    curr = board[row][col]
                    if curr == word[ctr]:
                        q.append((row + 1, col))
                        q.append((row - 1, col))
                        q.append((row, col + 1))
                        q.append((row, col - 1))
                        ctr += 1
                    else:
                        continue
        return False