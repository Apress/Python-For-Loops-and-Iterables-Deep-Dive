class SquareNumbers:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __next__(self):
        result = self.current ** 2
        if result >= self.end:
            raise StopIteration
        self.current += 1
        return result

    def __iter__(self):
        return SquareNumbers(self.end)

        # Previous (broken) version
        # return self


square_numbers = SquareNumbers(10)

for outer in square_numbers:
    for inner in square_numbers:
        print(f'Outer = {outer}, inner = {inner}')
