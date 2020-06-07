import sys
sys.stdin=open('in5.txt', 'rt')

n=int(input())
a = list(map(int, input().split()))
# 파이썬에서 round는 round_half_even 방식을 택한다.
# 반올림하는 숫자가 딱 절반일 경우 짝수쪽으로 근사값을 지정하는 방식.
# ex) 6.5 -> 6, 5.5 -> 6, 4.5 -> 4, 4.5111 -> 5
# 따라서 평균 구할때 round 쓰면 안됨.
# avg = round(sum(a) / n)
avg = int(sum(a)/n+0.5)
min = 2147000000 # 대충 가장 큰수
for idx, x in enumerate(a):
  tmp = abs(avg - x)
  if tmp < min:
    min = tmp
    res = idx + 1
    resScore = x
  elif tmp == min:
    if x > resScore:
      res = idx + 1
      resScore = x

print(avg, res)
