import sys
from collections import deque
sys.stdin = open("in5.txt", "r")

n = [list(map(int, input().split())) for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

Q = deque()
Q.append((0, 0, 0))

while len(Q):
  tmp = Q.popleft()
  a = tmp[0]
  b = tmp[1]
  cnt = tmp[2]
  if a == 6 and b == 6:
    print(cnt)
    sys.exit()
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    
    if 0 <= x <= 6 and 0 <= y <= 6 and n[x][y] == 0:
      Q.append((x, y, cnt + 1))
      n[x][y] = 1


print(-1)
