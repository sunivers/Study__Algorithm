import sys
sys.stdin = open('in5.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
add = 0
res = 0
for i in a:
  if i == 1:
    add += 1
    res += add
  else:
    add = 0

print(res)