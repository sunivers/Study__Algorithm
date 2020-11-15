import sys
sys.stdin = open("in5.txt", "r")

n, m = map(int, input().split())
s = []
for _ in range(n):
  x = list(map(int, input().split()))
  s.append(x)

large = 0

def DFS(L, score, time):
  global large
  if time > m:
    return
  if L == n:
    if score > large:
      large = score
  else:
    DFS(L+1, score + s[L][0], time + s[L][1])
    DFS(L+1, score, time)

DFS(0, 0, 0)
print(large)