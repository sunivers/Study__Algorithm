import sys
sys.stdin = open("in5.txt", "r")

# 컷엣지(Cut Edge) 적용하기
# 모든 요소의 합 : total
# 현재까지 판단한 요소들을 모두 더한 값 : tsum
# 판단 결과 YES인 요소들의 합 : sum
# sum + (total - tsum) : 현재까지 YES 판단된 요소들과, 전체에서 현재까지 판단한 값들을 제외한 남은 값들(앞으로 판단해야할 부분집합)을 더했을 때에도 현재까지 가장 큰 값 largest 보다 작다면 바로 리턴. - 남은 값들을 모두 더해도 가장 큰 값이 될 수 없기에.

c, n = map(int, input().split())
w = []
for _ in range(n):
  w.append(int(input()))

total = sum(w)

largest = 0
def DFS(i, sum, tsum):
  global largest
  if sum + (total - tsum) < largest:
    return
  if sum > c:
    return
  if i == n:
    if sum > largest:
      largest = sum
    return
  else:
    DFS(i + 1, sum + w[i], tsum + w[i])
    DFS(i + 1, sum, tsum + w[i])
    
DFS(0, 0, 0)
print(largest)
