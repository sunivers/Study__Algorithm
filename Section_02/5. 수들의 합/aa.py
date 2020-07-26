import sys
sys.stdin = open('in2.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
start = 0
i = 0
add = 0
res = 0
while start < len(a):
  add += a[i]
  i += 1

  if add == m:
    res += 1
    start += 1
    i = start
    add = 0
  
  if add > m:
    start += 1
    i = start
    add = 0

  if i == len(a):
    break

print(res)