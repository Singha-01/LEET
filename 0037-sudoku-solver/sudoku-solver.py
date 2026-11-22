class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    bit = 1 << (int(board[r][c]) - 1)
                    b = (r // 3) * 3 + c // 3
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[b] |= bit

        def backtrack():
            if not empty:
                return True

            best = 0
            min_count = 10

            for i, (r, c) in enumerate(empty):
                b = (r // 3) * 3 + c // 3
                available = 0x1FF & ~(rows[r] | cols[c] | boxes[b])
                count = available.bit_count()

                if count < min_count:
                    min_count = count
                    best = i

                if count == 1:
                    break

            if min_count == 0:
                return False

            r, c = empty.pop(best)
            b = (r // 3) * 3 + c // 3
            available = 0x1FF & ~(rows[r] | cols[c] | boxes[b])

            while available:
                bit = available & -available
                available -= bit

                num = bit.bit_length()
                board[r][c] = str(num)

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if backtrack():
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit

            board[r][c] = "."
            empty.insert(best, (r, c))
            return False

        backtrack()