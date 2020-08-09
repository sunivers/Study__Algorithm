import sys
sys.stdin = open('in5.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

start = 0
end = len(a) - 1
result = 0
while (start <= end):
  x = (start+ end) // 2
  if a[x] == m:
    result = x
    break

  # 강의영상에서는 없는 코드지만 이걸 써주면 반복이 1번이라도 더 줄어들 수 있음.
  # if a[start] == m:
  #   result = start
  #   break
  # elif a[end] == m:
  #   result = end
  #   break
  
  if a[x] > m:
    end = x - 1
  else:
    start = x + 1
    
print(result + 1)