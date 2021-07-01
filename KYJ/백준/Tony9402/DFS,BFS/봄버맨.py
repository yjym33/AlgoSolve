# 문제 출처 : https://www.acmicpc.net/problem/16918

import sys
from collections import deque

def loc_bombs(): # 폭탄의 위치를 찾아 bombs deque에 저장
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb.append((i, j))

def make_bombs(): # 모든 자리에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] == 'O'

def explode():      # bombs deque에 들어있는 좌표로 폭탄 터트림
    while bombs:
        r, c = bombs.popleft()
        board[r][c] = '.'
        if 0 <= r - 1:
            board[r - 1][c] = '.'
        if r + 1 < R:
            board[r + 1][c] = '.'
        if 0 <= c - 1:
            board[r][c - 1] = '.'
        if c + 1 < C:
            board[r][c + 1] = '.'

R, C, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

N -= 1  # 1초 동안 아무것도 하지 않는다
while N:
    bombs = deque()
    loc_bombs()
    make_bombs()
    N -= 1
    if N == 0:
        break
    explode()
    N -= 1

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()


# 다른풀이 

    import copy

# 입력값을 통해 폭탄의 시간을 가진 배열 채우기
def get_input():
    for i in range(R):
        tmp = str(input())
        for j in range(C):
            bomb[i][j] = 0 if tmp[j] == '.' else 2
            # 1초 동안 봄버맨은 아무것도 하지 않기 때문에 2를 넣어줌

# 0이면 '.' 1 2 3이면 '0'을 출력
def print_result():
    for i in range(R):
        for j in range(C):
            tmp = '.' if bomb[i][j] == 0 else 'O'
            print(tmp, end="")
        print()

# 비어있는 칸에 새로운 폭탄을 채우고 있는 칸은 1초 시간이 흐르도록 함
def fill_bomb(): 
    for i in range(R):
        for j in range(C):
            bomb[i][j] = 3 if bomb[i][j] == 0 else bomb[i][j] - 1

# 0이 된 칸은 주변의 폭탄도 제거
def bomb_explosion(bomb):
    bomb2 = copy.deepcopy(bomb)
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 0:
                if 0 <= j-1:
                    bomb2[i][j-1] = 0
                if j+1 < C:
                    bomb2[i][j+1] = 0
                if 0 <= i-1:
                    bomb2[i-1][j] = 0
                if i+1 < R:
                    bomb2[i+1][j] = 0
    return bomb2

R, C, N = map(int, input().split())
bomb = [[0 for _ in range(C)] for _ in range(R)]

if __name__=='__main__':
    get_input()
    for _ in range(N-1):
        fill_bomb()
        bomb = bomb_explosion(bomb)
    print_result()

# 순서 정리

# 1. 임의의 칸에 폭탄을 설치한다. - 3초
# 2. 처음 1초 동안 아무것도 하지 않는다.
# 3. 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치하고 폭탄의 시간이 0이 된 폭탄은 폭발한다.
# 4. 3번을 반복

# 풀이 순서
# 1. 입력받은 map을 통해 각 폭탄의 시간을 저장하고 있는 배열을 생성한다.
#    → 처음에 들어있는 폭탄의 시간은 2로 입력 (처음 1초는 아무일도 하지 않기 때문에)
# 2. N-1 초동안 아래의 과정을 반복 (처음 1초는 수행하지 않아도 되기 때문에 N-1)
# 3. 모든 폭탄의 시간을 -1 시킴
# 4. 비어있는 곳에 3초의 시간을 가지는 폭탄을 채움
# 5. 0이 된 폭탄이 있으면 주변 칸까지 0으로 수정폭탄의 시간을 가지고 있는 배열과 폭발이 모두 일어난 후를 저장할 배열을 구분시켜주어야함!
#    → deepcopy를 사용하지 않으면 0이 무한대로 퍼지는 문제가 발생하므로


