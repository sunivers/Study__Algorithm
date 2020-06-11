import sys
sys.stdin = open('in5.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))

def isPrime(x):
  if x == 1:
    return False
  # 소수 파악하려면 그 수의 절반까지만 계산해보면 된다.
  for i in range(2, x // 2 + 1):
    if x % i == 0:
      return False
  else:
    return True

def reverse(x):
  res=0
  while x > 0:
    t = x % 10
    res = res * 10 + t
    x = x // 10
  return res

for x in a:
  tmp = reverse(x)
  if isPrime(tmp):
    print(tmp, end=' ')
print()