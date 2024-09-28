pattern_size = int(input("Enter the size of the pattern: "))
x = 0
while x < pattern_size:
    y = 0
    for y in range(pattern_size):
        print('*', end='')
        y += 1
    print()
    x += 1