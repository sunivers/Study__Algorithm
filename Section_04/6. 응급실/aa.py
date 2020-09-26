import sys
sys.stdin = open('in5.txt', 'r')
from collections import deque

n, m = map(int, input().split())
danger = list(map(int, input().split()))
queue = deque([(idx, val) for idx, val in enumerate(danger)])
res = 0
while queue:
  cur = queue.popleft()
  for x in queue:
    if cur[1] < x[1]:
      queue.append(cur)
      break
  else:
    res += 1
    if cur[0] == m:
      print(res)
      break