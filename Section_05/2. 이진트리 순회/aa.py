def DFS(x):
  if x > 7:
    return
  else:
    print(x, end=' ') # 전위순회 출력 1 2 4 5 3 6 7
    DFS(x * 2)
    # print(x, end=' ') # 중위순회 출력 4 2 5 1 6 3 7
    DFS(x * 2 + 1)
    # print(x, end=' ') # 후위순회 출력 4 5 2 6 7 3 1

DFS(1)
print()