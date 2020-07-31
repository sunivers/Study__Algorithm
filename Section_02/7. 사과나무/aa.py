import sys
sys.stdin = open('in5.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# start, end 변수로 더할 범위를 지정
# 중간지점까지는 s는 작아지고 e는 커진다. 중간지점부터는 s는 커지고 e는 작아진다. (마름모 모양)
s = e = n // 2  # 몫만 구하고 싶을땐 나누기연산자 두개 (//)
total = 0
for i in range(n):
  for j in range(s, e+1):
    total += a[i][j]
  if i < n // 2:
    s -= 1
    e += 1
  else:
    s += 1
    e -= 1

print(total)
