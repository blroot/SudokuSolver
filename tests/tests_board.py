import unittest
from Board import Board


class TestBoard(unittest.TestCase):
    def test_empty_board(self):
        board = Board([[0, 8, 0, 5, 7, 6, 2, 0, 0],
                       [0, 0, 0, 4, 0, 2, 0, 0, 0],
                       [0, 0, 0, 0, 3, 9, 5, 4, 8],
                       [6, 3, 0, 9, 0, 0, 8, 5, 2],
                       [0, 9, 0, 2, 0, 0, 3, 7, 0],
                       [8, 0, 0, 0, 5, 0, 6, 9, 4],
                       [2, 5, 7, 6, 0, 3, 4, 8, 9],
                       [3, 0, 8, 7, 0, 0, 0, 2, 5],
                       [0, 4, 0, 0, 0, 0, 0, 0, 6]])

        self.assertFalse(board.is_full())

    def test_register_value(self):
        board = Board([[0, 8, 0, 5, 7, 6, 2, 0, 0],
                       [0, 0, 0, 4, 0, 2, 0, 0, 0],
                       [0, 0, 0, 0, 3, 9, 5, 4, 8],
                       [6, 3, 0, 9, 0, 0, 8, 5, 2],
                       [0, 9, 0, 2, 0, 0, 3, 7, 0],
                       [8, 0, 0, 0, 5, 0, 6, 9, 4],
                       [2, 5, 7, 6, 0, 3, 4, 8, 9],
                       [3, 0, 8, 7, 0, 0, 0, 2, 5],
                       [0, 4, 0, 0, 0, 0, 0, 0, 6]])

        board.register(0, 2, 1)

        self.assertEquals(1, board.get_solution[0][2])

    def test_delete(self):
        board = Board([[0, 8, 0, 5, 7, 6, 2, 0, 0],
                       [0, 0, 0, 4, 0, 2, 0, 0, 0],
                       [0, 0, 0, 0, 3, 9, 5, 4, 8],
                       [6, 3, 0, 9, 0, 0, 8, 5, 2],
                       [0, 9, 0, 2, 0, 0, 3, 7, 0],
                       [8, 0, 0, 0, 5, 0, 6, 9, 4],
                       [2, 5, 7, 6, 0, 3, 4, 8, 9],
                       [3, 0, 8, 7, 0, 0, 0, 2, 5],
                       [0, 4, 0, 0, 0, 0, 0, 0, 6]])

        board.register(0, 2, 1)
        board.delete()

        self.assertEquals(0, board.get_solution[0][2])

    def test_full(self):
        board = Board([[9, 8, 4, 5, 7, 6, 2, 1, 3],
                       [5, 1, 3, 4, 8, 2, 9, 6, 7],
                       [7, 2, 6, 1, 3, 9, 5, 4, 8],
                       [6, 3, 1, 9, 4, 7, 8, 5, 2],
                       [4, 9, 5, 2, 6, 8, 3, 7, 1],
                       [8, 7, 2, 3, 5, 1, 6, 9, 4],
                       [2, 5, 7, 6, 1, 3, 4, 8, 9],
                       [3, 6, 8, 7, 9, 4, 1, 2, 5],
                       [1, 4, 9, 8, 2, 5, 7, 3, 6]])

        self.assertTrue(board.is_full())

    def test_not_plausible_column(self):
        board = Board([[0, 8, 0, 5, 7, 6, 2, 0, 0],
                       [0, 0, 0, 4, 0, 2, 0, 0, 0],
                       [0, 0, 0, 0, 3, 9, 5, 4, 8],
                       [6, 3, 0, 9, 0, 0, 8, 5, 2],
                       [0, 9, 0, 2, 0, 0, 3, 7, 0],
                       [8, 0, 0, 0, 5, 0, 6, 9, 4],
                       [2, 5, 7, 6, 0, 3, 4, 8, 9],
                       [3, 0, 8, 7, 0, 0, 0, 2, 5],
                       [0, 4, 0, 0, 0, 0, 0, 0, 6]])

        self.assertFalse(board.is_plausible(1, 2, 7))
        self.assertFalse(board.is_plausible(7, 8, 6))
        self.assertFalse(board.is_plausible(0, 8, 2))

    def test_not_plausible_row(self):
        board = Board([[0, 8, 0, 5, 7, 6, 2, 0, 0],
                       [0, 0, 0, 4, 0, 2, 0, 0, 0],
                       [0, 0, 0, 0, 3, 9, 5, 4, 8],
                       [6, 3, 0, 9, 0, 0, 8, 5, 2],
                       [0, 9, 0, 2, 0, 0, 3, 7, 0],
                       [8, 0, 0, 0, 5, 0, 6, 9, 4],
                       [2, 5, 7, 6, 0, 3, 4, 8, 9],
                       [3, 0, 8, 7, 0, 0, 0, 2, 5],
                       [0, 4, 0, 0, 0, 0, 0, 0, 6]])

        self.assertFalse(board.is_plausible(0, 2, 6))
        self.assertFalse(board.is_plausible(3, 5, 5))
        self.assertFalse(board.is_plausible(5, 3, 8))

    def test_not_plausible_not_empty(self):
        board = Board([[0, 8, 0, 5, 7, 6, 2, 0, 0],
                       [0, 0, 0, 4, 0, 2, 0, 0, 0],
                       [0, 0, 0, 0, 3, 9, 5, 4, 8],
                       [6, 3, 0, 9, 0, 0, 8, 5, 2],
                       [0, 9, 0, 2, 0, 0, 3, 7, 0],
                       [8, 0, 0, 0, 5, 0, 6, 9, 4],
                       [2, 5, 7, 6, 0, 3, 4, 8, 9],
                       [3, 0, 8, 7, 0, 0, 0, 2, 5],
                       [0, 4, 0, 0, 0, 0, 0, 0, 6]])

        self.assertFalse(board.is_plausible(0, 1, 1))


if __name__ == '__main__':
    unittest.main()
