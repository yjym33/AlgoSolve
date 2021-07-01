# 문제 출처 : https://www.acmicpc.net/problem/16918

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


# 다른 풀이 2
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