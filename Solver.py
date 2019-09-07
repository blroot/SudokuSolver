class Solver:
    def __init__(self, board, target_solutions=None):
        self._board = board
        self._target_solutions = target_solutions - 1
        self._solutions = []

    def solve(self):
        if self._target_solutions is not None and self._target_solutions >= len(self._solutions):
            if self._board.is_full():
                self._solutions.append(self._board.solution)
            else:
                pos = self._board.find_next_available()
                i, j = pos
                for value in range(1, self._board.n + 1):
                    if self._board.is_plausible(i, j, value):
                        self._board.register(i, j, value)
                        self.solve()
                        self._board.delete(i, j)

    @property
    def solutions(self):
        return [row[:] for row in self._solutions]
