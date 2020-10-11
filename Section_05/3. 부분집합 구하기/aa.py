import sys
sys.stdin=open("in1.txt", "r")

# 강의 코드
# def DFS(v):
#     if v==n+1:
#         for i in range(1, n+1):
#             if ch[i]==1:
#                 print(i, end=' ')
#         print()
#     else:
#         ch[v]=1
#         DFS(v+1)
#         ch[v]=0
#         DFS(v+1)

# if __name__=="__main__":
#     n=int(input())
#     ch=[0]*(n+1)
#     DFS(1)
    

# 내 코드
n = int(input())
p = [0]*(n+1)

def DFS(v):
	if v > n:
		return
	else:
		# 해당 숫자 포함 되는 경우
		p[v] = 1
		DFS(v + 1)
		for i in range(1, n+1):
			if p[i] == 1:
				print(i, end=' ')
		print()
		# 해당 숫자 포함 안되는 경우
		p[v] = 0
		DFS(v + 1)

DFS(1)