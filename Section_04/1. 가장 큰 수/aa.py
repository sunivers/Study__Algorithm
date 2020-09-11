import sys
sys.stdin = open('in5.txt', 'r')

n, m = map(int, input().split())
n = list(map(int, str(n)))
stack = []  # 스택 자료 구조 이용

for x in n:
  # 스택에 있는 값이 나보다 작으면 제거
  while stack and m > 0 and x > stack[-1]:
    stack.pop()
    m -= 1
  stack.append(x)

if m > 0:
  stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)


