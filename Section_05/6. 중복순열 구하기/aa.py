import sys
sys.stdin = open("in1.txt", "r")

n, m = map(int, input().split())
res = [0]*m
cnt = 0

def DFS(L):
  global cnt
  if L == m:
    print(' '.join(res))
    cnt+=1
    return
  else:
    for x in range(1, n + 1):
      res[L] = str(x)
      DFS(L+1)

DFS(0)
print(cnt)