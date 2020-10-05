import sys
sys.stdin = open('in5.txt', 'r')

n = int(input())

def toBinary(n):
  if n != 0:
    toBinary(n // 2)
    print(n % 2, end='')
    
    
toBinary(n)
print()