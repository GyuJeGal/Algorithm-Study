import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
else:
    result = 2
    start, end = 2, 8
    while True:
        if n >= start and n < end:
            print(result)
            break
        else:
            start = end
            end += 6 * result
            result += 1