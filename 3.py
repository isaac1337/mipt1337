#first
def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fib(n - 2) + fib(n - 1)
n = int(input())
print(fib(n))

#second реализую алгоритм Ферма + дополнительно проверяю на простоту выданные им числа

from math import ceil
import numpy as np

def simplification(n):
    bebra = []
    x=ceil((n**0.5)) + 1
    while (int((x*x - n)**0.5)**2) != (x*x - n):
        x += 1
    y=int((x**2 - n)**0.5)
    a = x - y
    b = x + y
    bebra.append(a)
    bebra.append(b)
    return bebra
bb = simplification(int(input()))
def is_prime(x):
    for i in range(2, (x//2) + 1):
        if x % i == 0:
            return False
    return True
for j in bb:
    if is_prime(j) is True:
        continue
    else:
        bb.remove(j)
        bb = np.concatenate((np.array(bb), np.array(simplification(j))), axis=0)
print(bb)

#third реализую расширенный алгоритм Евклида

def euclid(a,b):
    if a == 0:
        return b, 0, 1
    d, u, v = euclid(b % a, a)
    x = v - (b // a ) * u
    y = u
    return d, x, y

a, b = map(int, input().split(" "))
print(euclid(a,b))

#fourth
def triangle(size, symb):
    r=-1
    b=[ [] for i in range (size)]
    for j in range(size):
        if j<(size//2+1):
            for k in range(int(j)+1):
                b[j].append(symb)
        else:
            r+=1
            for n in range((size//2-r)):
                b[j].append(symb)
    for m in range(size):
        print("".join(b[m]))
print(triangle(7, 'c'))

#fifth
N = int(input())
M = int(input())
a = [[0] * M for _ in range(N)]
x = 0
y = 0
dx = 1
dy = 0
for i in range(1, N * M + 1):
    a[y][x] = i
    test_x = x + dx
    test_y = y + dy
    if test_x >= M or test_y >= N or a[test_y][test_x] != 0:
        dx, dy = -dy, dx
    x += dx
    y += dy

for row in a:
    print(row)


#sixth
import numpy as np

ans = []
x = np.array(list(map(int, input().split())))
y = np.array(list(map(int, input().split())))
A = np.vstack([x, np.ones(len(x))]).T
ans.append(round(np.linalg.lstsq(A, y, rcond=None)[0][0],3))
ans.append(round(np.linalg.lstsq(A, y, rcond=None)[0][1],3))
print(ans)

#seventh
import numpy as np

N = int(input())
M = int(input())
matrix = []
column = []
for i in range(N):
    row = input().split()
    for j in range(M):
        row[j] = int(row[j])
    matrix.append(row)
for k in range(N):
    column.append(matrix[k][M - 1])
    matrix[k].pop(M - 1)
matrix = np.array(matrix)
column = np.array(column)
ans = np.linalg.solve(matrix, column)
print(ans)