class SquareNumbers:
    """
    Generates all square numbers
    starting at 1
    ending with the first square number
      equal to or greater than 'end'
    """
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
        return self

first_150_square_numbers = SquareNumbers(150)
for number in first_150_square_numbers:
    print(number)
print('Loop ended')
