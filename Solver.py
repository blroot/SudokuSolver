class Solver:
    def __init__(self, board):
        self._board = board
        self._solutions = []

    def solve(self):
        if self._board.is_full():
            self._solutions.append(self._board.solution)
        else:
            pos = self._board.find_next_available()
            i, j = pos
            for value in range(1, 10):
                if self._board.is_plausible(i, j, value):
                    self._board.register(i, j, value)
                    self.solve()
                    self._board.delete(i, j)

    @property
    def solutions(self):
        return [row[:] for row in self._solutions]
