class Board:
    def __init__(self, data):
        self._data = data
        self._n = len(self._data[0])

    def is_full(self):
        for row in self._data:
            for i in row:
                if i == 0:
                    return False
        return True

    def register(self, i, j, value):
        self._data[i][j] = value

    def column_iterator(self):
        columns = range(self._n)
        return iter(columns)

    def delete(self, i, j):
        self._data[i][j] = 0

    def find_next_available(self):
        for i in range(self._n):
            for j in range(self._n):
                if self._data[i][j] == 0:
                    return i, j
        return False

    def is_plausible(self, i, j, value):
        # if i-1 >= 0 and 0 in self._data[i-1]:
        #    return False

        column = [self._data[x][j] for x in range(self._n)]
        sub_index = self._sub_board_index(i, j)
        sub_board = self._sub_board(sub_index)

        if self._data[i][j] == 0 \
                and (value not in column and value not in self._data[i] and value not in sub_board):
            return True
        else:
            return False

    @staticmethod
    def _sub_board_index(i, j):
        sub_board_index = [0, 0]
        if i in [0, 1, 2]:
            sub_board_index[0] = 0
        elif i in [3, 4, 5]:
            sub_board_index[0] = 1
        elif i in [6, 7, 8]:
            sub_board_index[0] = 2

        if j in [0, 1, 2]:
            sub_board_index[1] = 0
        elif j in [3, 4, 5]:
            sub_board_index[1] = 1
        elif j in [6, 7, 8]:
            sub_board_index[1] = 2

        return sub_board_index

    def _sub_board(self, index):
        if index == [0, 0]:
            return self._data[0][0:3] + self._data[1][0:3] + self._data[2][0:3]
        if index == [0, 1]:
            return self._data[0][3:6] + self._data[1][3:6] + self._data[2][3:6]
        if index == [0, 2]:
            return self._data[0][6:9] + self._data[1][6:9] + self._data[2][6:9]

        if index == [1, 0]:
            return self._data[3][0:3] + self._data[4][0:3] + self._data[5][0:3]
        if index == [1, 1]:
            return self._data[3][3:6] + self._data[4][3:6] + self._data[5][3:6]
        if index == [1, 2]:
            return self._data[3][6:9] + self._data[4][6:9] + self._data[5][6:9]

        if index == [2, 0]:
            return self._data[6][0:3] + self._data[7][0:3] + self._data[8][0:3]
        if index == [2, 1]:
            return self._data[6][3:6] + self._data[7][3:6] + self._data[8][3:6]
        if index == [2, 2]:
            return self._data[6][6:9] + self._data[7][6:9] + self._data[8][6:9]

    def print(self):
        string = ""
        for row in self._data:
            for i in row:
                string += str(i) + "|"
            string += "\n"

        print(string)

    @property
    def solution(self):
        return [row[:] for row in self._data]

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return str(self._data)
