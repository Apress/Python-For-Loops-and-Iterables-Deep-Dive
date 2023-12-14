names = ['Aarav', 'Bianca', 'Carlos']
names_iterator = iter(names)
print(next(names_iterator))  # Aarav
print(next(names_iterator))  # Bianca
print(next(names_iterator))  # Carlos
print(next(names_iterator))  # StopIteration exception

# Above equivalent to
# for name in names:
#     print(name)
