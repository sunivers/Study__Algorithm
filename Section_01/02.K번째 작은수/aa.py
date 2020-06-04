import sys
sys.stdin=open('in1.txt', 'rt')

case = int(input())
for a in range(case):
  n, s, e, k = map(int, input().split())
  b = list(map(int, input().split()))
  c = b[s-1:e]
  c.sort()
  print('#%d %d' %(a+1, c[k-1]))