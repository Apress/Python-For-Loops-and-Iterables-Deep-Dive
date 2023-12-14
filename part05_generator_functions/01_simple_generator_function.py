def greetings():
    yield 'Hello'
    yield 'Good'
    yield 'morning'

for word in greetings():
    print(word)

print('=-' * 10)

greetings_iterator = greetings()
print(next(greetings_iterator))  # Hello
print(next(greetings_iterator))  # Good
print(next(greetings_iterator))  # Morning
print(next(greetings_iterator))  # Exception: StopIteration
