x = int(input())
number = 0
total = 0
while x > 1:
    x = x-1
    for digit in str(x):
        if (int(digit) == 2):
            total = total + 1
            if (int(digit) == 8):
                total = total - 1
        if (int(digit) == 8):
            total = total + 1
print(total)
