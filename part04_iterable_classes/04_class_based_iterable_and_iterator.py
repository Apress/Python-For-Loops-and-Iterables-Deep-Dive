class SquareNumbersIterator:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __next__(self):
        result = self.current ** 2
        if result >= self.end:
            raise StopIteration
        self.current += 1
        return result


class SquareNumbersIterable:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return SquareNumbersIterator(self.end)


square_numbers_iterable = SquareNumbersIterable(10)

for outer in square_numbers_iterable:
    for inner in square_numbers_iterable:
        print(f'Outer = {outer}, inner = {inner}')
