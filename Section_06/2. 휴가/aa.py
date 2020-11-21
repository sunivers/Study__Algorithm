import sys
sys.stdin = open("in5.txt", "r")

n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(n):
  a, b = map(int, input().split())
  t[i+1] = a
  p[i+1] = b
res = 0

def DFS(L, P):
  # L 날짜
  global res
  if L == n + 1:
    if res < P:
      res = P
  else:
    if L + t[L] <= n + 1:
      DFS(L + t[L], P + p[L])
    DFS(L + 1, P)
    
DFS(1, 0)
print(res)