squares = (n ** 2 for n in range(100))

# Generator expressions don't have a length
print(len(squares))  # TypeError: object of type 'generator' has no len()

# You can't use indexing with generator expressions
print(squares[2])  # TypeError: 'generator' object is not subscriptable

# Only use a generator expression once
print(min(squares))  # 0
print(max(squares))  # ValueError: max() arg is an empty sequence
