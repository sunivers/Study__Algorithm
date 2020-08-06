import sys
sys.stdin = open('in5.txt', 'rt')

def check(a):
  # 행(ch1) 열(ch2) 체크
  for i in range(9):
    ch1 = [0] * 10
    ch2 = [0] * 10
    for j in range(9):
      ch1[a[i][j]] = 1
      ch2[a[j][i]] = 1

    if sum(ch1) != 9 or sum(ch2) != 9:
      return False

  # 그룹 체크
  for i in range(3):
    for j in range(3):
      ch3 = [0] * 10
      for k in range(3):
        for l in range(3):
          ch3[a[i * 3 + k][j * 3 + l]] = 1
      
      if sum(ch3) != 9:
        return False
  
  return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
  print('YES')
else:
  print('NO')