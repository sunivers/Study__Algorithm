import sys
sys.stdin = open('in5.txt', 'rt')

n, m = map(int, input().split())
dic={}
for i in range(1, n+1):
  for j in range(1, m+1):
    if (i + j) in dic:
      dic[i + j] += 1
    else:
      dic[i + j] = 1

maxval = max(list(dic.values()))

for key, value in dic.items():
  if value == maxval:
    print(key, end=' ')
print()