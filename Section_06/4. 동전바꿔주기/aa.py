import sys
sys.stdin = open("in5.txt", "r")

t = int(input())
k = int(input())
p = []
n = []
for _ in range(k):
  a, b = map(int, input().split())
  p.append(a)
  n.append(b)

res = 0

def DFS(L, sum):
  global res
  if sum > t:
    return
  if sum == t:
    res += 1
    return
  if L == k:
    return
  else:
    for i in range(n[L]+1):
      DFS(L + 1, sum + (p[L] * i))

DFS(0, 0)
print(res)