import sys
sys.stdin = open("in1.txt", "r")

def Count(size):
  cnt = 1
  sum = 0
  for x in Music:
    if sum + x > size:
      cnt += 1
      sum = x
    else:
      sum += x

  return cnt


n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music)
lt = maxx # DVD 최소용량은 적어도 가장 긴 곡보다는 커야 한다.
rt = sum(Music)
res = 0

while (lt <= rt):
  mid = (lt + rt) // 2
  if Count(mid) <= m:
    res = mid
    rt = mid - 1
  else:
    lt = mid + 1

print(res)