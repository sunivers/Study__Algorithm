import sys
sys.stdin = open("in5.txt", "r")

n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0

def DFS(L, s, sum):
  global cnt
  if L == k:
    if sum % m == 0:
      cnt += 1
    return
  else:
    for i in range(s, n):
      DFS(L+1, i+1, sum+a[i])

DFS(0, 0, 0)
print(cnt)