import sys
from collections import deque
sys.stdin = open('in5.txt', 'r')

need = list(input())
n = int(input())
plan = [input() for _ in range(n)]

for i, p in enumerate(plan):
  cur = 0
  for j, x in enumerate(p):
    if x in need:
      for y in range(0, cur + 1):
        if x == need[y]:
          cur += 1
          break
      else:
        print('#%d NO' % (i + 1))
        break
    if j == len(p) - 1:
      if cur == len(need):
        print('#%d YES' % (i + 1))
      else:
        print('#%d NO' % (i + 1))