def square_numbers(end):
    number = 0
    while (squared := number ** 2) <= end:
        yield squared
        number += 1


for outer in square_numbers(10):
    for inner in square_numbers(10):
        print(f'Outer = {outer}, inner = {inner}')

# Code for Python 3.7 or older
# def square_numbers(end):
#     number = 0
#     squared = number ** 2
#     while squared <= end:
#         yield squared
#         number += 1
#         squared = number ** 2
