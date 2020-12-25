import sys
from collections import deque
sys.stdin = open("in5.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 기준 좌표로 부터 4방향으로 뻗어가기 위해 더해줄 좌표값
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ch = [[0] * n for _ in range(n)] # [[0]*n]*n 이렇게 하면 각 행이 참조값으로 생성되기 때문에 반드시 for문으로 넣어준다.
sum = 0
sum += a[n//2][n//2]
Q = deque()
Q.append((n // 2, n // 2))
ch[n // 2][n // 2] = 1
L = 0

while True:
  if L == n // 2:
    break
  L += 1
  size = len(Q)
  for i in range(size):
    target = Q.popleft()
    for j in range(4):
      x = target[0] + dx[j]
      y = target[1] + dy[j]
      if ch[x][y] == 0:
        ch[x][y] = 1
        sum += a[x][y]
        Q.append((x, y))
        
      
print(sum)
