import sys
sys.stdin = open("in5.txt", "r")

n, m = map(int, input().split())
a = [0] * m
chk = [0] * (n + 1)
cnt = 0

def DFS(i, L):
  global a, chk, cnt
  if L == m:
    for x in a:
      print(x, end=' ')
    print()
    cnt += 1
    chk[i] = 0
    return
  else:
    chk[i] = 1
    for x in range(1, n + 1):
      if chk[x] == 0:
        a[L] = x
        DFS(x, L + 1)
    chk[i] = 0

DFS(0, 0)
print(cnt)