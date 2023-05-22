class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solution = []

    def solve(self):
        if self._solve(0):
            self._print_solution()
        else:
            print("No solution found.")

    def _solve(self, col):
        if col == self.n:
            return True

        for row in range(self.n):
            if self._is_safe(row, col):
                self.board[row][col] = 1
                if self._solve(col + 1):
                    self.solution.append((row, col))
                    return True
                self.board[row][col] = 0

        return False

    def _is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def _print_solution(self):
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if (row, col) in self.solution:
                    line += "Q "
                else:
                    line += ". "
            print(line)


# Usage example
n = 8  # Board size
queens = NQueens(n)
queens.solve()
