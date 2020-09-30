import sys
sys.stdin = open('in4.txt', 'r')

w1 = input()
w2 = input()
word = dict()
for x in w1:
  # get은 딕셔너리에 해당 키가 없을 경우 에러를 뱉지않고 두번째 인자로 넘긴 디폴트값을 리턴한다.
  word[x] = word.get(x, 0) + 1

for x in w2:
  if x in word:
    word[x] -= 1

for val in word.values():
  if val > 0:
    print('NO')
    break
else:
  print('YES')