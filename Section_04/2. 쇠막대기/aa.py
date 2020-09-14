import sys
sys.stdin = open('in5.txt', 'r')

pipe=input()
stack = []
last = ''
res = 0
for x in pipe:
  if x == '(':
    stack.append(x)
  else:
    stack.pop()
    if last == '(':
      res += len(stack)
    else:
      res += 1

  last = x

print(res)