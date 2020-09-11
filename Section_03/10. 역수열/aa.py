import sys
sys.stdin = open('in5.txt', 'r')

n = int(input())
m = list(map(int, input().split()))

res = [0 for _ in range(n)]

# 배열 0으로 초기화 하는법 2
# res = [0]*n

for i in range(n):
  cnt = 0
  for j in range(n):
    if res[j] == 0:
      if cnt == m[i]:
        res[j] = i + 1
        break
      cnt += 1

print(res)
