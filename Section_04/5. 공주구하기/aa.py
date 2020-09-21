import sys
sys.stdin = open('in1.txt', 'r')

n, k = map(int, input().split())

# 내가 짠 코드 - 리스트 이용
# 그러나 리스트는 pop() 하면 밀리는 연산이 있고, deque는 없기 때문에 더 효율적.
# queue = list(range(n))
# cnt = 0
# while len(queue) > 1:
#   cnt += 1
#   if cnt == k:
#     cnt = 0
#     queue.pop(0)
#   else:
#     queue.append(queue.pop(0))
# print(queue.pop()+1)


# 강의 코드
from collections import deque

dq = list(range(1, n+1))
dq = deque(dq)
while dq:
  for _ in range(k - 1):
    tmp = dq.popleft()
    dq.append(tmp)
  dq.popleft()

  if len(dq) == 1:
    print(dq.popleft())
  

