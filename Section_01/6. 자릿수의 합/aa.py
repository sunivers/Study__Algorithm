import sys
sys.stdin = open('in5.txt', 'rt')

def digit_sum(x):
  
  # 몫과 나머지를 이용한 방법
  # sum = 0
  # while x>0:
  #   sum += x%10
  #   x = x//10
  # return sum

  # 문자열로 변환하는 방법
  sum = 0
  for i in str(x):
    sum += int(i)
  return sum

n = int(input())
nums = list(map(int, input().split()))
maxSum = 0
res = 0
for x in nums:
  a = digit_sum(x)
  if maxSum < a:
    maxSum = a
    res = x

print(res)