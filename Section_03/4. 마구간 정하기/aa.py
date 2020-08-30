import sys
sys.stdin = open("in5.txt", "r")

def Count(len):
  cnt = 1
  ep = Line[0]
  for i in range(1, n):
    if Line[i] - ep >= len:
      cnt += 1
      ep = Line[i]
  return cnt

n, c = map(int, input().split())
Line = [int(input()) for _ in range(n)]
Line.sort()
lt = 1
rt = max(Line)
res = 0
while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= c:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1
  
print(res)
