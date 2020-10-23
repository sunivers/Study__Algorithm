import sys
sys.stdin = open("in4.txt", "r")

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
m = int(input())

res = 500
def DFS(cnt, sum):
  global res
  if cnt > res:
    return
  if sum == m:
    if cnt < res:
      res = cnt
    return
  elif sum > m:
    return
  else:
    for x in a:
      DFS(cnt+1, sum+x)

DFS(0, 0)

print(res)