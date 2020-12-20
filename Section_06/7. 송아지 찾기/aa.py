import sys
sys.stdin = open("in5.txt", "r")

# 강의용 코드
from collections import deque
n, m = map(int, input().split())
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
ch[n] = 1
dis[n] = 0 # 시작점으로부터 몇 번만에 이동하는지
dQ = deque()
dQ.append(n)
while dQ:
  now = dQ.popleft()
  if now == m:
    break
  for next in (now - 1, now + 1, now + 5):
    if 0 < next < MAX:
      if ch[next] == 0:
        dQ.append(next)
        ch[next] = 1
        dis[next] = dis[now] + 1
    
print(dis[m])


# 내가 짠 코드는 파이썬 재귀호출 제한(1000번)에 걸려서 일부 문제가 실행이 안된다ㅠ_ㅠ
# 그리고 DFS와 다르게 BFS는 재귀호출처럼 뎁스 우선 탐색을 하면 안된다.
# S, E = map(int, input().split())
# res = 10000
# def DFS(cnt, sum):
#   global res
#   if sum == E:
#     if cnt < res:
#       res = cnt
#     return
#   else:
#     if sum < E:
#       DFS(cnt + 1, sum + 5)
#       DFS(cnt + 1, sum + 1)
#     else:
#       DFS(cnt + 1, sum - 1)
      
# DFS(0, S)
# print(res)