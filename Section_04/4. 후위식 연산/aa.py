import sys
sys.stdin = open('in5.txt', 'r')

a = input()
stack = []

for x in a:
  if x.isdecimal():
    stack.append(int(x))
  else:
    r = stack.pop()
    l = stack.pop()
    if x == '+':
      stack.append(l + r)
    elif x == '-':
      stack.append(l - r)
    elif x == '*':
      stack.append(l * r)
    elif x == '/':
      stack.append(l / r)
    
print(stack.pop())