import sys
sys.stdin = open('in5.txt', 'r')

n = int(input())
player = []
for _ in range(n):
  h, w = map(int, input().split())
  player.append((h, w))

player.sort(reverse=True) # 키를 기준으로 내림차순 정렬

largest = 0
cnt = 0
for h, w in player:
  # 키는 이미 정렬됐기 때문에 몸무게만 비교하면 됨.
  # 나보다 키큰 사람이랑만 비교하면 됨.
  if w > largest:
    largest = w
    cnt += 1

print(cnt)