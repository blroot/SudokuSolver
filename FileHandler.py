import csv
from exceptions import InvalidRowLength, NotAnInteger, NotAValidInteger
from Board import Board
import pickle


class FileHandler:
    def __init__(self, source, results):
        self._boards_dict = {}
        self.source_file = source
        self.results_file = results

    def read_boards_file_csv(self):
        with open(self.source_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            board_number = 0
            row_count = 0
            board = []
            for index, row in enumerate(csv_reader):
                if len(row) != 9:
                    raise InvalidRowLength(index)

                try:
                    row = [int(x) for x in row]
                except ValueError:
                    raise NotAnInteger

                for i in row:
                    if i < 0 or i > 9:
                        raise NotAValidInteger

                row_count += 1
                board.append(row)

                if row_count == 9:
                    self._boards_dict.setdefault(board_number, board)
                    board = []
                    row_count = 0
                    board_number += 1

    def write_results_to_file(self, results):
        with open(self.results_file, mode="w") as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            for key in results:
                result = results.get(key)
                for board in result:
                    csv_writer.writerows(board)

    def persist(self, results, dump_name):
        # Se reemplazan los tableros ya resueltos
        for key in results:
            self._boards_dict[key] = results.get(key)[0]

        pickle.dump(self._boards_dict, open(dump_name, "wb"))

    def load_boards_file_dump(self):
        self._boards_dict = pickle.load(open(self.source_file, "rb"))

    @property
    def boards_count(self):
        return len(self._boards_dict.keys())

    def get_board(self, index):
        return [row[:] for row in self._boards_dict.get(index)]
