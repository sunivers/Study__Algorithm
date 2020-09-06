import sys
sys.stdin = open('in5.txt', 'r')

# 내가 짠 방식 (이게 더 효율적인거 같다...? 새로운 자료구조를 알려주기 위해 pop 방식을 사용한 것일까...)
n, m = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()
s = 0
e = n - 1
cnt = 0
while (s <= e):
  if weight[s] + weight[e] <= m:
    s += 1
    e -= 1
    cnt += 1
  else:
    e -= 1
    cnt += 1

print(cnt)


# 강의에서 사용한 방식 (deque 자료구조 이용)

import sys
# 일반 list의 경우 pop(0)으로 맨 앞 자료를 꺼낼 경우 뒤에 있던 자료들을 한 칸씩 앞으로 땡겨주는 연산을 하기 때문에 비효율적임.
# deque의 경우 자료를 땡겨주는 대신 가르키는 포인터만 변경해줘서 더 효율적이다.
from collections import deque

sys.stdin=open("input.txt", "r")
n, limit=map(int, input().split())
p = list(map(int, input().split()))

p.sort()
p=deque(p) # 리스트를 deque화 시킴.
cnt=0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft() # 일반 list의 경우 pop(0)로 해줬던 것을 deque는 popleft()로 써주면 된다.
        p.pop()
        cnt+=1
print(cnt)
