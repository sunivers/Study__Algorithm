import sys
sys.stdin = open("in5.txt", "r")

n = int(input())
road = [[0] * n for _ in range(n)]
ch = [[0] * n for _ in range(n)]
min = 2147000000
max = 0
sp = (0, 0)
ep = (0, 0)

for i in range(n):
  tmp = list(map(int, input().split()))
  for j in range(n):
    if tmp[j] < min:
      min = tmp[j]
      sp = (i, j)
    if tmp[j] > max:
      max = tmp[j]
      ep = (i, j)
    road[i][j] = tmp[j]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def DFS(x, y):
  global cnt
  if x == ep[0] and y == ep[1]:
    cnt += 1
  else:
    for i in range(4):
      a = x + dx[i]
      b = y + dy[i]
      if 0 <= a < n and 0 <= b < n and ch[a][b] == 0 and road[a][b] > road[x][y]:
        ch[a][b] = 1
        DFS(a, b)
        ch[a][b] = 0


ch[sp[0]][sp[1]] = 1
DFS(sp[0], sp[1])
print(cnt)