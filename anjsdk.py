# DO NOT MODIFY
def triangle(h):
    # Write your code here

    # DO NOT MODIFY
    pass

height = int(input("Height: "))

for i in range (1, height + 1):
    print(' ' * (height - i), end=' ')
    print('*' * (2 * i - 1))