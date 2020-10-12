import sys
sys.stdin=open("in4.txt", "r")

n = int(input())
a = list(map(int, input().split()))
total = sum(a)

def DFS(v, sum):
	if sum > total // 2:
		# 시간 복잡도를 줄이기 위한 코드.
		# 각 부분집합의 합이 같으려면 총 합의 반 이상이 될 수 없다.
		return
	if v == n:
		if sum == (total - sum):
			print('YES')
			sys.exit(0) # 프로그램 종료
	else:
		DFS(v + 1, sum + a[v])
		DFS(v + 1, sum)
		
DFS(0, 0)
print('NO')