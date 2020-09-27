import sys
from collections import deque
sys.stdin = open('in1.txt', 'r')

need = list(input())
n = int(input())

for i in range(n):
  cur = 0
  plan = input()
  for j, x in enumerate(plan):
    if x in need:
      for y in range(0, cur + 1):
        if x == need[y]:
          cur += 1
          break
      else:
        print('#%d NO' % (i + 1))
        break
  else:
    if cur == len(need):
      print('#%d YES' % (i + 1))
    else:
      print('#%d NO' % (i + 1))