import csv
from exceptions import InvalidRowLength, NotAnInteger, NotAValidInteger
from Board import Board


class CsvHandler:
    def __init__(self, source="boards.csv", results="results.csv"):
        self.boards_dict = {}
        self.source_file = source
        self.results_file = results

    def read_boards_file(self):
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
                    self.boards_dict.setdefault(board_number, Board(board))
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
