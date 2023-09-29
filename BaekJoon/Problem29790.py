import sys

input = sys.stdin.readline

N, U, L = map(int, input().split())

if N >= 1000:
    if U >= 8000 or L >= 260:
        print('Very Good')
    else:
        print('Good')
else:
    print('Bad')

### 5분

