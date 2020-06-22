import sys
sys.stdin = open('in5.txt', 'rt')

res=0
for x in input():
  if x.isdecimal():
    res = res * 10 + int(x)
    
print(res)

cnt=0
for i in range(1, res+1):
  if res % i == 0:
    cnt += 1
    
print(cnt)