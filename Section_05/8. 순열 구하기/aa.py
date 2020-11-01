import sys
sys.stdin = open("in5.txt", "r")

n, m = map(int, input().split())
res = [0] * m
chk = [0] * (n + 1)
cnt = 0

def DFS(L):
  global res, chk, cnt
  if L == m:
    for x in res:
      print(x, end=' ')
    print()
    cnt += 1
    return
  else:
    for i in range(1, n + 1):
      if chk[i] == 0:
        chk[i] = 1
        res[L] = i
        DFS(L + 1)
        chk[i] = 0

DFS(0)
print(cnt)