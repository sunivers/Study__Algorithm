import sys
sys.stdin = open('in5.txt', 'r')

n = int(input())
word = dict()
for _ in range(n):
  word[input()] = 1

for _ in range(n - 1):
  word[input()] = 0

for key, value in word.items():
  if value != 0:
    print(key)