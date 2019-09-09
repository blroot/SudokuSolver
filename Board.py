import math


class Board:
    def __init__(self, data):
        self._data = data
        self._n = len(self._data[0])
        self._r = int(math.sqrt(self._n))

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
        column = [self._data[x][j] for x in range(self._n)]
        in_box = self._is_in_box(i - i % self._r, j - j % self._r, value)

        if self._data[i][j] == 0 and (value not in column and value not in self._data[i] and not in_box):
            return True
        else:
            return False

    def _is_in_box(self, i, j, value):
        for k in range(self._r):
            for l in range(self._r):
                if self._data[k + i][l + j] == value:
                    return True
        return False

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

    @property
    def n(self):
        return self._n

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

