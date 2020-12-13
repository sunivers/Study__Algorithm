import sys
sys.stdin = open("in5.txt", "r")

##### 강의 코드 #####
# 1 ~ 26 까지 돌면서 한자리 또는 두자리 해당되는 수가 있으면 res에 추가.
# 이렇게 하면 0에 대한 예외 처리를 별도로 안해줘도 된다.

code = list(map(int, input()))
n = len(code)
code.insert(n, -1) # 마지막 인덱스일 경우 L+1 에 접근할 때 에러를 막기 위한 조치
res = [0]*n
cnt = 0

def _DFS(L, P):
  global cnt
  if L == n:
    cnt += 1
    for j in range(P):
      print(chr(res[j] + 64), end='')
    print()
  else:
    for i in range(1, 27):
      if code[L] == i:
        res[P] = i
        _DFS(L + 1, P + 1)
      elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
        _DFS(L + 2, P + 1)

_DFS(0, 0)
print(cnt)



##### 내가 짠 코드 #####
n = list(map(int, input()))
code = ['']
for i in range(26):
  code.append(chr(65 + i))
  
res = []

def DFS(L, str):
  if L >= len(n):
    res.append(str)
    return
  else:
    # 바로 다음 0이 올 경우 예외처리
    if (L + 1 < len(n) and n[L + 1] == 0):
      DFS(L + 2, str + code[n[L]*10])
      return

    DFS(L + 1, str + code[n[L]])

    # 다다음 0이 올 경우 예외처리
    if (L + 2 < len(n) and n[L + 2] == 0):
      return

    if L < len(n)-1:
      tmp = n[L]*10 + n[L+1]
      if tmp <= 26:
        DFS(L + 2, str + code[tmp])

DFS(0, '')
for str in res:
  print(str)
print(len(res))