import sys
sys.stdin = open("in5.txt", "r")

# 방향그래프이기 때문에 자기자신보다 작은 숫자의 정점이라도 갈 수 있다.

n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
ch = [0] * (n + 1)

for _ in range(m):
  x, y = map(int, input().split())
  g[x][y] = 1

cnt = 0
def DFS(v):
  global cnt
  if v == n:
    cnt += 1
    return
  else:
    for i in range(1, n+1):
      if v != i and ch[i] == 0 and g[v][i] == 1:
        ch[i] = 1
        DFS(i)
        ch[i] = 0

ch[1] = 1
DFS(1)

print(cnt)