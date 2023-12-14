"""
List all numbers n between 1 and 100
where both n^2 and n^4 start with the digit '1'
"""

def start_with_1(n):
    return str(n)[0] == '1'


for i in range(1, 100):
    square_i = i ** 2
    if not start_with_1(square_i):
        continue

    square_square_i = square_i ** 2
    if not start_with_1(square_square_i):
        continue

    print(f'{i:2} squared is {square_i:4}, and again {square_square_i:7}')

    # Previous version
    # square_i = i ** 2
    # if start_with_1(square_i):
    #     square_square_i = square_i ** 2
    #     if start_with_1(square_square_i):
    #         print(f'{i:2} squared is {square_i:4}, and again {square_square_i:7}')
