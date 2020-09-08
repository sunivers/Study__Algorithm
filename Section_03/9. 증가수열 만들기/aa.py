import sys
sys.stdin = open('in5.txt', 'r')

n = int(input())
m = list(map(int, input().split()))

l = 0
r = n - 1
last = 0
cnt = 0
res = ''

# 강의 코드
while l <= r:
  tmp = []
  if m[l] > last:
    tmp.append((m[l], 'L'))
  if m[r] > last:
    tmp.append((m[r], 'R'))
  tmp.sort()
  if len(tmp) == 0:
    break
  else:
    res += tmp[0][1]
    last = tmp[0][0]
    if tmp[0][1] == 'L':
      l += 1
    else:
      r -= 1

print(len(res))
print(res)


  # 내가 짠 코드 ㅠ_ㅠ
  # if m[l] <= last and m[r] <= last:
  #   break

  # if m[l] > last and m[l] < m[r]:
  #   last = m[l]
  #   l += 1
  #   cnt += 1
  #   res += 'L'
  # elif m[r] > last and m[r] < m[l]:
  #   last = m[r]
  #   r -= 1
  #   cnt += 1
  #   res += 'R'
  # elif m[l] > m[r]:
  #   last = m[l]
  #   l += 1
  #   cnt += 1
  #   res += 'L'
  # else:
  #   last = m[r]
  #   r -= 1
  #   cnt += 1
  #   res += 'R'

# print(cnt)
# print(res)