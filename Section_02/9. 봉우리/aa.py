import sys
sys.stdin = open('in1.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 나의 풀이
def isPeaks(i, j):
  t = b = l = r = 0
  
  if i - 1 >= 0:
    t = a[i - 1][j]
  if i + 1 < n:
    b = a[i + 1][j]
  if j - 1 >= 0:
    l = a[i][j - 1]
  if j + 1 < n:
    r = a[i][j + 1]

  if a[i][j] > t and a[i][j] > b and a[i][j] > l and a[i][j] > r:
    return True
  
  return False

count = 0
for i in range(n):
  for j in range(n):
    if isPeaks(i, j):
      count += 1

print(count)


# 강의 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 가장자리 0으로 초기화
a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
  x.insert(0, 0)
  x.append(0)

cnt = 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    # all() 함수는 모든 조건을 만족해야 True
    if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
      cnt += 1

print(cnt)


