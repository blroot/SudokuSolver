import unittest
from Solver import Solver
from Board import Board


class MyTestCase(unittest.TestCase):
    def test_solve9x9(self):
        sudoku = [[0, 8, 0, 5, 7, 6, 2, 0, 0],
                  [0, 0, 0, 4, 0, 2, 0, 0, 0],
                  [0, 0, 0, 0, 3, 9, 5, 4, 8],
                  [6, 3, 0, 9, 0, 0, 8, 5, 2],
                  [0, 9, 0, 2, 0, 0, 3, 7, 0],
                  [8, 0, 0, 0, 5, 0, 6, 9, 4],
                  [2, 5, 7, 6, 0, 3, 4, 8, 9],
                  [3, 0, 8, 7, 0, 0, 0, 2, 5],
                  [0, 4, 0, 0, 0, 0, 0, 0, 6]]
        expected_solution = [[9, 8, 4, 5, 7, 6, 2, 1, 3],
                             [5, 1, 3, 4, 8, 2, 9, 6, 7],
                             [7, 2, 6, 1, 3, 9, 5, 4, 8],
                             [6, 3, 1, 9, 4, 7, 8, 5, 2],
                             [4, 9, 5, 2, 6, 8, 3, 7, 1],
                             [8, 7, 2, 3, 5, 1, 6, 9, 4],
                             [2, 5, 7, 6, 1, 3, 4, 8, 9],
                             [3, 6, 8, 7, 9, 4, 1, 2, 5],
                             [1, 4, 9, 8, 2, 5, 7, 3, 6]]
        board = Board(sudoku)
        solver = Solver(board)
        solver.solve()
        solution = solver.solutions[0]
        self.assertEqual(expected_solution, solution)


if __name__ == '__main__':
    unittest.main()
