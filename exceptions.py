class InvalidRowLength(Exception):
    def __init__(self, row_number):
        self.row_number = row_number
        super(InvalidRowLength, self).__init__()


class NotAnInteger(Exception):
    pass


class NotAValidInteger(Exception):
    pass

