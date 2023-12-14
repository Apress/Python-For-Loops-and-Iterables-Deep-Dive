import time


def show_time(prompt):
    print(f'{time.time() - start_time:.06f}: {prompt}')


start_time = time.time()

show_time('Starting')

numbers = range(50_000_000)
show_time('Range of numbers created')

squares = (number ** 2 for number in numbers)
show_time('List of squares created')

# Previous version:
# squares = [number ** 2 for number in numbers]

for square in squares:
    if square > 50_000:
        break
show_time('Value found')
print('Result: ', square)
