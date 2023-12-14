def greetings():
    print('In greetings(), before Hello')
    yield 'Hello'

    print('In greetings(), before Good')
    yield 'Good'

    print('In greetings(), before morning')
    yield 'morning'

    print('Done')

for word in greetings():
    print('In top level code', word, '\n')
