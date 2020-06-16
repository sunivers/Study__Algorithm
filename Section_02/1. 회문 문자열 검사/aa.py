import sys
sys.stdin = open('in5.txt', 'rt')

n = int(input())
for i in range(n):
  a = input().upper()
  leng = len(a)
  for j in range(leng // 2):
    # 마이너스 인덱스는 요소를 거꾸로 찾는다.
    if a[j] != a[-1-j]:
      print('#%d NO' % (i + 1))
      break
  else:
    print('#%d YES' % (i + 1))
    
# 좀 더 파이썬스러운 방법 (그러나 위에 방법이 정석이다)
# for i in range(n):
#   a = input().upper()
#   if a == a[::-1]:
#     print('#%d YES' % (i + 1))
#   else:
#     print('#%d NO' % (i + 1))
