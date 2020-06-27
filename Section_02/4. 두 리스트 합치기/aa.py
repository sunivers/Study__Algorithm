import sys
sys.stdin = open('in3.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 두 배열 더하고 sort() 하는 문제가 아님. 
# 이미 정렬된 두 배열을 정렬하는 것은 시간복잡도가 O(n)이기 때문에 sort()하는 것 보다 훨씬 빠름.
# res = a + b
# res.sort()

p1 = p2 = 0
res = []
# for _ in range(n + m):
while p1<n and p2<m:
  if a[p1] < b[p2]:
    res.append(a[p1])
    p1 += 1
  else:
    res.append(b[p2])
    p2 += 1

if p1 == n:
  res = res + b[p2:]
if p2 == m:
  res = res + a[p1:]

for x in res:
  print(x, end=' ')
print()