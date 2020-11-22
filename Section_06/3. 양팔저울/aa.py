import sys
sys.stdin = open("in5.txt", "r")

k = int(input())
a = list(map(int, input().split()))
s = sum(a)
res = set()
def DFS(L, sum):
  global res
  if L == k:
    # 음수는 판단하지 않는다. (양팔 저울 양쪽을 바꾸면 대응되는 양수값이 나오기 때문.)
    if 0 < sum <= s:
      res.add(sum)
  else:
    # 양팔저울 왼쪽에 놓는 경우
    DFS(L + 1, sum + a[L])
    # 양팔저울 오른쪽에 놓는 경우
    DFS(L + 1, sum - a[L])
    # 양팔저울에 놓지 않는 경우
    DFS(L + 1, sum)

DFS(0, 0)
print(s - len(res))
