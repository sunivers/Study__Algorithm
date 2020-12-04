import sys
sys.stdin = open("in1.txt", "r")

n = int(input())
a = []
for _ in range(n):
  a.append(int(input()))

m = [0]*3
res = 2147000000

def DFS(L):
  global res
  if L == n:
    chk = set()
    for x in m:
      chk.add(x)
    if len(chk) != 3:
      return
    tmp = max(m) - min(m)
    if tmp < res:
      res = tmp
    return
  else:
    for i in range(3):
      m[i] += a[L]
      DFS(L + 1)
      m[i] -= a[L]

DFS(0)
print(res)