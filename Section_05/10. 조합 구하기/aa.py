import sys
sys.stdin = open("in5.txt", "r")

def DFS(L, s):
  global cnt
  if L == m:
    for i in range(m):
      print(res[i], end=' ')
    cnt += 1
    print()
    return
  else:
    for i in range(s, n + 1):
      res[L] = i
      DFS(L + 1, i + 1)

n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0, 1)

print(cnt)