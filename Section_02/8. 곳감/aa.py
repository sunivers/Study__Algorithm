import sys
sys.stdin = open('in1.txt', 'rt')

n = int(input())
gam = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
  h, t, k = map(int, input().split())
  if t == 0:
    for _ in range(k):
      gam[h - 1].append(gam[h - 1].pop(0))
  else:
    for _ in range(k):
      gam[h - 1].insert(0, gam[h - 1].pop())

s = 0
e = n - 1
total = 0
for i in range(n):
  for j in range(s, e + 1):
    total += gam[i][j]
  
  if i < n // 2:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1

print(total)
