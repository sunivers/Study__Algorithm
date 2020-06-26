import sys
sys.stdin = open('in5.txt', 'rt')

arr = list(range(21))

for _ in range(10):
  a, b = map(int, input().split())
  for i in range((b - a + 1) // 2):
    arr[a + i], arr[b - i] = arr[b - i], arr[a + i];

arr.pop(0)  # 그냥 pop() 하면 맨 뒤에 요소 삭제, 인덱스 넘겨주면 해당 인덱스 삭제
for x in arr:
  print(x, end=' ')

print()