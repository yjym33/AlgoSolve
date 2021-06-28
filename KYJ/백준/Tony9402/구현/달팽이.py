# 문제 출처 : https://www.acmicpc.net/problem/1913

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

dr = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위쪽 순서대로 
dc = [1, 0, -1, 0]

r = n//2 # 시작 row
c = n//2 # 시작 column
num = 1 # 해당 위치에 들어간 숫자 1씩 증가 예정
len = 0 # 특정 방향으로 이동할 거리, 얼마나 이동할 것인가. for문으로 동일작업 수행가능함

board[r][c] = num

while True:
    for i in range(4):
        for _ in range(len): # 특정방향으로 한칸씩 이동하며 숫자입력
            r += dr[i]
            c += dc[i]
            num += 1
            board[r][c] = num
            if num == m: # 찾을 번호의 인덱스를 저장
                ans = [r+1, c+1]
    if r == c == 0:
        break
    r -= 1
    c -= 1
    len += 2

for i in range(n):
    print(*board[i])
print(*ans)

# 이 문제는 아래와 같은 방식으로 진행이되는것 같고, 다음과 같이 이해를 했다.

# 문제에서 설명해주는 예시일때 1을 기준으로 봤을 때 위, 아래는 1과 column 인덱스가 동일하고 row 인덱스가 하나씩 차이난다.
# 즉 1 = a[1][3] 이면 위의 인덱스는 a[0][3] 아래는 a[2][3] 이라는 것 [x, y] 좌표로 본다면 x값이 1씩 차이가 난다.
# 반대로 좌, 우는 row인덱스가 동일하고 column 인덱스가 1개씩 차이가 난다. (y값이 차이가 난다.)
# 즉 1 = a[1][3] 이면 좌 = a[1][2], 우 = a[1][4]가 된다.

# 즉 1을 기준으로 상 (-1, 0), 하(1, 0), 좌(0, -1), 우(0, 1) 차이가 난다.
# 그래서 이를 배열에 담으면 [오른쪽, 아래쪽, 왼쪽, 위쪽] 순서대로 나타난다.
# 이 문제에서는 방향전환을 하기 위해서 dr 에 [상, 하]를  배열 dc 에 [좌, 우]가 담긴 배열을 만들었다.

# 그리고 len의 길이만큼 특정 방향으로 이동을 하면서 숫자를 입력하고 이동하면서 숫자를 늘려준다.

# 반복하면서 돌다가 찾을 번호의 인덱스를 저장하여 ans 값에 저장해준다.


# 참고하면 좋을만한 링크 
# https://jennnn.tistory.com/3 (푸는 방식이 비슷함)