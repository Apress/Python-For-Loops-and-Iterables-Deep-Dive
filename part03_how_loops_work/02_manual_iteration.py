names = ['Amara', 'Bruno', 'Chen', 'Dimitri', 'Esra', 'Fatima']

# Start of manual 'for' code
# Does the same as: for name in names
names_iterator = iter(names)
while True:
    try:
        name = next(names_iterator)
    except StopIteration:
        break
    # End of manual 'for' code

    # Rest of the code is the block
    # which is executed for each name
    print(name)
