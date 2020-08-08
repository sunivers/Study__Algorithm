import sys
sys.stdin = open('in5.txt', 'rt')

a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(7):
  for j in range(3):
    if a[i][j] == a[i][4 + j] and a[i][j + 1] == a[i][4 + j - 1]:
      cnt += 1
    if a[j][i] == a[4 + j][i] and a[j + 1][i] == a[4 + j - 1][i]:
      cnt += 1

print(cnt)

    