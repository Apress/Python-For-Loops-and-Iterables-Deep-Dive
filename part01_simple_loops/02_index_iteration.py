# For loop in C
# for (int i = 0; i < length; i++) {
#     printf("%s\n", names[i]);
# }

names = 'Liam', 'Diego', 'Ananya', \
    'Natalia', 'Kofi', 'Yuki', \
    'Thabo', 'Jens', 'Charlotte', 'Félix'

# Don't do this
for index in range(len(names)):
    print('Hello', names[index])

# Don't do this either
index = 0
while index < len(names):
    print('Hello', names[index])
    index += 1

# Do this instead
for name in names:
    print('Hello', name)
