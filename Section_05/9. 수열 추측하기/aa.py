import sys
sys.stdin = open("in5.txt", "r")

# 1         2         3         4
#     1+2       2+3       3+4
#        1+2+2+3   2+3+3+4
#         1+2+2+3+2+3+3+4
#               ==
#         1+(2*3)+(3*3)+4
# 이런 형식으로 계산하면 결국 각 숫자에 순서대로 1, 3, 3, 1을 곱한 값과 같다.
# 여기서 파스칼의 삼각형을 이용한다.
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# 이런식으로 각 숫자에 곱할 값(이항계수)을 미리 배열에 담아두고 연산해주면 된다.

def DFS(L, sum):
  if L == n and sum == f:
    for i in range(n):
      print(p[i], end=' ')
    print()
    sys.exit()
  else:
    for m in range(1, n + 1):
      if ch[m] == 0:
        ch[m] = 1
        p[L] = m
        DFS(L + 1, sum+(p[L]*b[L]))
        ch[m] = 0
      

n, f = map(int, input().split())
p = [0] * n
b = [1] * n # 곱할 값 저장할 배열 (이항계수의 양쪽 맨 끝은 항상 1이기 때문에 1로 초기화)
ch = [0] * (n + 1)
for i in range(1, n):
  b[i] = b[i - 1] * (n - i) // i  # 이항계수 구하는 코드 (그냥 외우자... 앞에 있는 값에 n-i 값을 곱한걸 i로 나누면 된다.)

DFS(0, 0)


