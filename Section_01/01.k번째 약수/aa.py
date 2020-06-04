import sys
sys.stdin=open('in5.txt', 'rt')

n, k = map(int, input().split())
cnt=0
for a in range(1, n+1):
  if n%a==0:
    cnt+=1
  if cnt==k:
    print(a)
    break
else:
  print(-1)